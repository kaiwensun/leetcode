#!/usr/bin/env python3

import functools
import os
import re
import requests
import collections
import datetime
import urllib
import sys
import json
import time
from enum import Enum
from requests_html import HTMLSession
import pyppeteer

UNRECOGNIZED_CONTEST_SOLUTIONS = {}
README_FILENAME = "README.md"
ONLINE_MAP = {}
DB_PROBLEMS = None
LOCAL_MAP = collections.defaultdict(list)
NOT_BACKFILLED = set()
ATTEMPTED = {891, 964, 1397, 1655}
STARRED = {315, 321, 391, 630, 805, 913, 1199, 1713, 1819, 1923, 2040}

NOT_BACKFILLED = {str(item) for item in NOT_BACKFILLED}
ATTEMPTED = {str(item) for item in ATTEMPTED}
STARRED = set(map(str, STARRED))


def get_root_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Client:
    def __init__(self):
        self.session = HTMLSession()

    def getJson(self, url):
        ex = None
        res = self.session.get(url)
        for _ in range(3):
            try:
                time.sleep(1)
                res.html.render()
                break
            except pyppeteer.errors.NetworkError as e:
                ex = e
        else:
            raise ex
        text = res.html.find("html")[0].text
        return json.loads(text)

# ======== Modeling ========


class GraphQLData:
    BASE_URL = "https://leetcode.com"
    GRAPHQL_URL = BASE_URL + "/graphql"

    def __init__(self):
        self.client = None
        self.csrf = None

    def _query(self):
        if self.csrf is None:
            self.client = requests.Session()
            self.client.get(GraphQLData.BASE_URL)
            self.csrf = self.client.cookies['csrftoken']
        params = {
            'operationName': "query",
            'variables': self.variables,
            'query': 'query ' + self.query_str
        }
        return self.client.post(GraphQLData.GRAPHQL_URL, json=params, headers={
            "X-CSRFToken": self.csrf, "Referer": GraphQLData.BASE_URL})


class Question:

    """
    A class modeling online questions fetched from API
    """

    US_QUESTION_URL_PATTERN = "https://leetcode.com/problems/%s"
    CN_QUESTION_URL_PATTERN = "https://leetcode-cn.com/problems/%s"
    DIFFICULTIES = ["Easy", "Medium", "Hard"]
    QID_SPLIT = 5000  # new weekly contest questions have very big question ids

    def __init__(self, dic):
        self._id = str(dic["stat"]["frontend_question_id"])

        self._contest_temp_id = None
        self._title = dic["stat"]["question__title"].strip()
        # malformatted title from api
        self._title = " ".join(self._title.split())

        self._lock = dic["paid_only"]
        self._difficulty = dic["difficulty"]["level"]
        self._slug = dic["stat"]["question__title_slug"]
        self._is_mock_dic = dic.get("_is_mock_dic", False)
        self._correct_new_weekly_contest_question()

    def is_mock(self):
        return self._is_mock_dic

    def difficulty(self):
        return Question.DIFFICULTIES[self._difficulty - 1]

    def is_us(self):
        return self._id.isdigit()

    def cn_url(self):
        return Question.CN_QUESTION_URL_PATTERN % self._slug

    def us_url(self):
        return Question.US_QUESTION_URL_PATTERN % self._slug

    def id(self):
        return self._id

    def title(self):
        return self._title

    def lock(self):
        return self._lock

    def is_contest(self):
        return self.is_us() and int(self.id()) > Question.QID_SPLIT

    def _correct_new_weekly_contest_question(self):
        if self.is_contest() and not self._is_mock_dic:
            qd = QuestionDetails(self._slug)
            light = qd.query_light()
            if light:
                light["title"] = light["title"].strip()
                if light["title"] != self.title():
                    print(
                        "[WARN] Failed to correct the question data for %s: QuestionDetails titles don't match." % self.id())
                elif str(light["questionFrontendId"]) == self.id():
                    print(
                        "[WARN] Failed to correct the question data for %s: ID from QuestionDetails is same." % self.id())
                else:
                    new_id = str(light["questionFrontendId"])
                    print("[WARN] Correct the question ID: %s -> %s" %
                          (self.id(), new_id))
                    self._contest_temp_id, self._id = self._id, new_id
            else:
                print(
                    "[WARN] Failed to correct the question data for %s: QuestionDetails data not found." % self.id())

    def order(self):
        if self.is_us():
            return (-int(self.id()),)
        else:
            return (float("inf"), self.id())

    def __str__(self):
        return "%s, %s, %s" % (self.id(), self.title(), self.us_url())


class Solution:

    """
    A class modeling loca solution files"
    """

    FOLDER_SIZE = 500
    KNOWN_TYPES = {"c", "cpp", "java", "py", "ts",
                   "rb", "sh", "js", "sql", "php", "txt", "md"}
    KNOWN_CN_GROUPS = [
        re.compile("^LCS \d{2}$"),
        re.compile("^LCP \d{2}$"),
        re.compile("^剑指 Offer II \d{3}$"),
        re.compile("^剑指 Offer \d{2}( ?- I{1,3})?$"),
        re.compile("^面试题 \d{2}\.\d{2}$"),
        re.compile("^DD-\d{7}")
    ]
    ROOT_PATH = None
    moved_cnt = 0

    def __init__(self, abs_path):
        if not Solution.ROOT_PATH:
            Solution.ROOT_PATH = get_root_path()
        self._abs_path = abs_path
        self._abs_folder, self._basename = os.path.split(abs_path)
        self._parse_basename()

    def is_in_root(self):
        return self._abs_folder == Solution.ROOT_PATH

    def type(self):
        return self._basename.split(".")[-1]

    def id(self):
        if self.is_us():
            return str(int(self._id))
        else:
            return self._id

    def original_abs_path(self):
        return self._abs_path

    def is_contest(self):
        return self.is_us() and int(self.id()) > Question.QID_SPLIT

    def _parse_basename(self):
        # id.title[.version][.hint].typ
        splited = self._basename.split(".")
        if len(splited) > 2 and re.match("^面试题 \d{2}$", splited[0]) and re.match("^\d{2}$", splited[1]):
            splited[0] += "." + splited[1]
            splited.pop(1)
        if len(splited) > 5:
            raise ValueError("Unable to parse basename %s" % self._basename)
        for i in range(len(splited)):
            splited[i] = splited[i].strip()
            if not splited[i] and not self.is_contest():
                raise ValueError("Empty piece in file %s" % self._basename)
        self._typ = splited[-1]
        if self._typ not in Solution.KNOWN_TYPES:
            raise ValueError("Unknown file type for %s" % self._basename)

        self._id = splited[0]
        self._set_question()
        self._desired_folder = self._calc_desired_folder()
        self._title = self._version = self._hint = None
        for piece in splited[1:-1]:
            if piece.isdigit():
                if self._version is not None:
                    raise ValueError(
                        "Found multiple versions from basename %s" % self._basename)
                self._version = piece
            elif piece[0] == "(" and piece[-1] == ")":
                if self._hint is not None:
                    raise ValueError(
                        "Found multiple hints from basename %s" % self._basename)
                self._hint = piece[1:-1]
                if not self._hint:
                    raise ValueError(
                        "The hint in basename cannot be empty for %s" % self._basename)
            else:
                if self._title is not None:
                    raise ValueError(
                        "Found multiple titles from basename %s" % self._basename)
                self._title = piece.strip()
        question = getattr(self, "_question", None)
        if question is None:
            msg = "Unable to auto-detect title from online source, for the basename %s" % self._basename
            if self.is_contest():
                print("[WARN] " + msg)
            else:
                raise ValueError(msg)
        if self._title is None:
            if question is None:
                if self.is_contest():
                    self._title = ""
                else:
                    raise ValueError(
                        "Unable to correct Solution name %s. Wait for contest to end." % self._basename)
            else:
                # trying to fill the title from online source
                print("[WARN] Solution %s name defaults to %s" %
                      (self.id(), question.title()))
                self._title = question.title()
        else:
            if question and self._title != question.title():
                raise ValueError("file name doesn't match online question title: (online: %s, local: %s, basename: %s)" % (
                    question.title(), self._title, self._basename))

    def mock_question_for_unrecognized_contest_solution(self):
        return Question({
            "_is_mock_dic": True,
            "stat": {
                "frontend_question_id": self.id(),
                "question__title": self._title or f"contest question {self.id()}",
                "question__title_slug": None
            },
            "paid_only": False,
            "difficulty": {
                "level": None
            }
        })

    def is_us(self):
        return self._id.isdigit()

    def desired_folder(self):
        return self._desired_folder

    def _calc_desired_folder(self):
        if self.is_us():
            num = int(self._id)
            start = (num - 1) // Solution.FOLDER_SIZE * \
                Solution.FOLDER_SIZE + 1
            end = start + Solution.FOLDER_SIZE - 1
            return "{:04d}-{:04d}".format(start, end)
        elif any(matcher.match(self._id) for matcher in Solution.KNOWN_CN_GROUPS):
            folders = ["LCS", "LCP", "剑指 Offer II", "剑指 Offer", "面试题", "DD"]
            for folder in folders:
                if self._id.startswith(folder):
                    return folder
            else:
                raise Exception("fail to assign a folder")
        else:
            raise ValueError("Unknown question id %s" % self._id)

    def desired_abs_path(self):
        if self.is_contest():
            return os.path.join(Solution.ROOT_PATH, self.desired_basename())
        else:
            return os.path.join(Solution.ROOT_PATH, self.desired_folder(), self.desired_basename())

    def is_misplaced(self):
        return self._abs_path != self.desired_abs_path()

    def correct_location(self):
        if not os.path.exists(self.desired_folder()):
            print("creating", self.desired_folder())
            os.mkdir(self.desired_folder())
        if os.path.exists(self.desired_abs_path()):
            raise Exception("Destination already exists: %s -> %s" %
                            (self._abs_path, self.desired_abs_path()))
        print("Moving %s -> %s" % (self._abs_path, self.desired_abs_path()))
        os.rename(self._abs_path, self.desired_abs_path())
        Solution.moved_cnt += 1

    def desired_basename(self):
        res = ["{:04d}".format(int(self._id)) if self.is_us() else self._id,
               self._title]
        if self.is_contest() and not self._title:
            # during contest, not easy to determine the title. this is to avoid double dots in file names
            res.pop()
        if self._version is not None:
            res.append(self._version)
        if self._hint is not None:
            res.append("(" + self._hint + ")")
        res.append(self._typ)
        return ".".join(res)

    def _set_question(self):
        if self.id() in ONLINE_MAP:
            self._question = ONLINE_MAP[self.id()]
        else:
            for q in ONLINE_MAP.values():
                if q.is_us() and q._contest_temp_id == self.id():
                    self._question = q
                    self._id = q.id()
                    break
            else:
                if self.is_contest():
                    print(
                        "[WARN] Unable to auto-detect title from online source for %s. Probably a new weekly contest question." % self._basename)
                    UNRECOGNIZED_CONTEST_SOLUTIONS[self.id()] = self
                else:
                    raise ValueError(
                        "Unable to auto-detect title from online source, for the basename %s", self._basename)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return str({
            "id": self._id,
            "type": self._typ,
            "title": self._title,
            "version": self._version,
            "hint": self._hint,
            "abs_path": self._abs_path,
            "abs_folder": self._abs_folder,
            "desired_folder": self._desired_folder,
            "basename": self._basename,
            "is_in_root": self.is_in_root()
        })


class QuestionDetails(GraphQLData):
    LIGHT_QUERY = """
        query($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionFrontendId
                title
                titleSlug
            }
        }"""

    FULL_QUERY = """
        query($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                boundTopicId
                title
                titleSlug
                content
                translatedTitle
                translatedContent
                isPaidOnly
                difficulty
                likes
                dislikes
                isLiked
                similarQuestions
                contributors {
                    username
                    profileUrl
                    avatarUrl
                    __typename
                }
                topicTags {
                    name
                    slug
                    translatedName
                    __typename
                }
                companyTagStats
                codeSnippets {
                    lang
                    langSlug
                    code
                    __typename
                }
                stats
                hints
                solution {
                    id
                    canSeeDetail
                    paidOnly
                    hasVideoSolution
                    __typename
                }
                status
                sampleTestCase
                metaData
                judgerAvailable
                judgeType
                mysqlSchemas
                enableRunCode
                enableTestMode
                enableDebugger
                envInfo
                libraryUrl
                adminUrl
                __typename
            }
        }
    """

    def __init__(self, titleSlug):
        self.titleSlug = titleSlug
        self.variables = {'titleSlug': self.titleSlug}
        super().__init__()

    def query_light(self):
        self.query_str = QuestionDetails.LIGHT_QUERY
        return self._query().json()['data']['question']

    def query_full(self):
        # do not abuse
        self.query_str = QuestionDetails.FULL_QUERY
        return self._query().json()['data']['question']


class Topic(GraphQLData):
    TOPIC_URL_PATTERN = "https://leetcode.com/discuss/topic/%d"
    query_str = """
        query($topicId: Int!) {
            topic(id: $topicId) {
                id
                viewCount
                topLevelCommentCount
                subscribed
                title
                pinned
                tags
                hideFromTrending
                post {
                ...DiscussPost
                __typename
                }
                __typename
            }
        }

        fragment DiscussPost on PostNode {
            id
            content
            updationDate
            creationDate
            status
            author {
                username
            }
            __typename
        }"""

    def __init__(self, topic_id):
        self.topic_id = int(topic_id)
        self.variables = {'topicId': self.topic_id}
        super().__init__()

    def query(self):
        resp = self._query().json()
        title = resp['data']['topic']['title']
        content = resp['data']['topic']['post']['content']
        creation_time = resp['data']['topic']['post']['creationDate']
        creation_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime(creation_time))
        update_time = resp['data']['topic']['post']['updationDate']
        update_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime(update_time))
        return {
            "title": title,
            "content": content,
            "creation_time": creation_time,
            "update_time": update_time
        }

    @functools.lru_cache(1)
    def get_topic_url(self):
        # 301 redirect
        resp = requests.get(Topic.TOPIC_URL_PATTERN % self.topic_id)
        return resp.url

    def get_title_slug(self):
        topic_url = self.get_topic_url()
        pattern = r"(?<=^https://leetcode.com/problems/).*(?=/discuss/" + \
            str(self.topic_id) + "/.*$)"
        # print(self.topic_id, topic_url)
        return re.search(pattern, topic_url).group()

    @functools.lru_cache(1)
    def get_question_id(self):
        qd = QuestionDetails(self.get_title_slug())
        light = qd.query_light()
        return light["questionFrontendId"]

    @functools.lru_cache(1)  # generate at most once
    def generate_local_file(self):
        root_path = get_root_path()
        qid = self.get_question_id()
        question = ONLINE_MAP[qid]
        file_name = "%s.%s.md" % (qid, question.title())
        abs_path = os.path.join(root_path, file_name)
        param = self.query()
        param["content"] = param["content"].replace(
            '\\n', '\n').replace('\\t', '\t')
        param["link"] = self.get_topic_url()
        param["topic_id"] = self.topic_id

        metadata = "\n".join(["> Source: [{topic_id}]({link})",
                              ">",
                              "> Created at: {creation_time}",
                              ">",
                              "> Updated at: {update_time}"])

        file_content = "\n\n".join(["# {title}",
                                    metadata,
                                    "----",
                                    "{content}"]).format(**param)
        with open(abs_path, "w") as out:
            out.write(file_content)
            print("[INFO] Generated discussion at %s" % abs_path)
            print(param["title"])


class TopicManager(GraphQLData):
    FILTER_OUT = [496542, 866365, 673853]

    query_str = """
        query($username: String!, $limit: Int) {
            userRecentTopics(username: $username, limit: $limit) {
                id
                title
                commentCount
                post {
                creationDate
                voteCount
                __typename
                }
                __typename
            }
        }
    """

    def __init__(self, username, limit=20):
        self.username = username
        self.limit = limit
        self.variables = {'username': self.username, 'limit': self.limit}
        super().__init__()

    @functools.lru_cache(1)
    def query(self):
        return self._query().json()['data']['userRecentTopics']

    def get_topic_ids(self):
        resp = self.query()
        return [item["id"] for item in resp if item["id"] not in TopicManager.FILTER_OUT]

    def get_topics(self):
        return [Topic(topic_id) for topic_id in self.get_topic_ids()]

    def generate_local_files(self):
        for topic in self.get_topics():
            topic.generate_local_file()


# ======== readme ========


def update_file(relative_path, content):
    root_path = get_root_path()
    abs_path = os.path.join(root_path, relative_path)
    if not os.path.isfile(abs_path):
        raise Exception("Cannot find file: %s" % abs_path)
    with open(abs_path, "w") as out:
        out.write(content)

# ======== markdowne ========


class MarkdownType(Enum):
    MAIN_README = "MAIN_README"
    TODO_PROBS = "TODO_PROBS"
    FULL_TABLE = "FULL_TABLE"


MAIN_README_SIZE = 2000
all_items_file_name = "full_table.md"


def gen_markdown(questions, solutions, title, markdown_type):

    CN_FLAG = ":cn:"
    US_FLAG = ":us:"
    STAR = ":star:"
    LOCK = ":lock:"
    DB = " sql "
    CHECK_MARK = ":heavy_check_mark:"
    QUESTION_MARK = ":question:"

    def gen_markdown_questions(questions):
        size_limit = ""
        if markdown_type == MarkdownType.MAIN_README:
            all_items_file_path = os.path.join("others", all_items_file_name)
            size_limit = (f"The following table contains only the latest {MAIN_README_SIZE} items. "
                          f"For a full list, check [{all_items_file_name}]({all_items_file_path}). "
                          "This is because GitHub currently limits blob rendering of a repo's README to around 500 KB of data."
                          )
        header = """
|Status|#|Title|Question Links|My Solutions|Difficulty ([CN](https://leetcode-cn.com/problemset/all))|
|:---|:---|:---|:---|:---|:---|
"""
        if markdown_type == MarkdownType.MAIN_README:
            questions = questions[:MAIN_README_SIZE]
        body = "\n".join(gen_markdown_question_row(question)
                         for question in questions)
        return size_limit + header + body

    def gen_markdown_question_row(question):

        def get_status(question):
            qid = question.id()
            status = ""
            if LOCAL_MAP[qid] or qid in NOT_BACKFILLED:
                if qid in ATTEMPTED:
                    print(
                        "[WARN] question %s is in ATTEMPTED but it is believed to be solved" % qid)
                if LOCAL_MAP[qid] and qid in NOT_BACKFILLED:
                    print(
                        "[WARN] question %s is in NOT_BACKFILLED but a solution is found" % qid)
                status += CHECK_MARK
            if qid in ATTEMPTED:
                status += QUESTION_MARK
            if question.lock():
                status += LOCK
            if qid in STARRED:
                status += STAR
            if qid in DB_PROBLEMS:
                status += DB
            return status

        def get_solution_links(question):
            res = []
            for sol in sorted(LOCAL_MAP[question.id()], key=lambda sol: [sol.type(), sol.desired_basename()]):
                if sol.is_us() and int(sol.id()) > 5000:
                    relative_link = urllib.parse.quote(sol.desired_basename())
                else:
                    relative_link = "/".join([urllib.parse.quote(sol.desired_folder()),
                                              urllib.parse.quote(sol.desired_basename())])
                res.append("[%s](%s)" % (sol.type(), relative_link))
            if not res and question.id() in NOT_BACKFILLED:
                return "(not uploaded yet)"
            return ", ".join(res)

        def get_us_question_link(question):
            if question.is_mock():
                return ""  # mock does not have url and slug
            if question.is_us():
                return "[%s](%s)" % (US_FLAG, question.us_url())
            else:
                return ""

        def get_cn_question_link(question):
            if question.is_mock():
                return ""  # mock does not have url and slug
            return "[%s](%s)" % (CN_FLAG, question.cn_url())

        row = [
            "",
            get_status(question),
            question.id(),
            question.title(),
            " ".join(item for item in [get_us_question_link(
                question), get_cn_question_link(question)] if item),
            get_solution_links(question),
            "" if question.is_mock() else question.difficulty(),
            ""
        ]
        return "|".join(row)

    def gen_markdown_stats(questions, solutions):
        total = len(questions)
        solved = len({sol.id() for sol in solutions} | NOT_BACKFILLED)
        attempted = len(ATTEMPTED)
        unsolved_without_lock = len([q for q in questions if (
            q.is_us()
            and not q.lock()
            and q.id() not in NOT_BACKFILLED
            and q.id() not in DB_PROBLEMS
            and not LOCAL_MAP[q.id()])])
        unsynced = len(NOT_BACKFILLED)
        starred = len(STARRED)
        line1 = "|Total|Solved|Attempted|US site non-DB unsolved w/o lock|"
        line2 = "|:---:|:---:|:---:|:---:|"
        line3 = "|%s|%s|%s|%s|"
        args = [total, solved, attempted, unsolved_without_lock]

        if unsynced:
            line1 += "Not synced to GitHub"
            line2 += ":---:|"
            line3 += "%s|"
            args.append(unsolved_without_lock)
        if starred:
            line1 += "Starred"
            line2 += ":---:|"
            line3 += "%s|"
            args.append(starred)
        return "\n".join(["", line1, line2, line3, ""]) % tuple(args)

    def gen_markdown_intro():

        def gen_markdown_site_links():
            return """
* LeetCode websites
  * [leetcode.com](https://leetcode.com/)
  * [leetcode-cn.com](https://leetcode-cn.com/)
"""

        def gen_markdown_self_link():
            if markdown_type == MarkdownType.MAIN_README:
                rel_path = os.path.join(
                    os.path.relpath(__file__, get_root_path()))
            else:
                rel_path = os.path.join(os.path.relpath(
                    __file__, os.path.join(get_root_path(), "others")))

            return "* This report is generated by [%s](%s)." % (os.path.basename(__file__), rel_path)

        def gen_markdown_today():
            return "* Last updat: " + datetime.date.today().strftime("%A, %B %d, %Y").replace(" 0", " ")

        def gen_support():
            if markdown_type == MarkdownType.MAIN_README:
                return "* :gift_heart: [Buy me a coffee](others/support/README.md)"
            elif markdown_type == MarkdownType.FULL_TABLE:
                return "* :gift_heart: [Buy me a coffee](support/README.md)"
            return ""

        res = ["# " + title,
               gen_markdown_site_links(),
               gen_markdown_self_link(),
               gen_markdown_today(),
               gen_support()]
        return "\n".join(res)

    def gen_markdown_language_stats(solutions):
        DO_NOT_STATS = {"txt", "sql", "sh", "md"}
        cnt = collections.Counter(
            sol.type() for sol in solutions if sol.type() not in DO_NOT_STATS)
        sm = sum(cnt.values())
        if sm == 0:
            return ""
        line1 = line2 = line3 = "|"
        for lang, lan_cnt in cnt.most_common():
            line1 += lang + "|"
            line2 += ":---:|"
            line3 += "%.1f%%|" % (lan_cnt * 100 / float(sm))
        return "\n".join(["", line1, line2, line3, ""])

    res = [
        gen_markdown_intro(),
        gen_markdown_stats(questions, solutions),
        gen_markdown_language_stats(solutions),
        gen_markdown_questions(questions)
    ]
    return "\n".join(res)


# ======== load resources ========

def load_resources(client, offline):

    def save_online_resource(json_dict, abs_path):
        with open(abs_path, "w") as out:
            json.dump(json_dict, out, indent=2)

    def load_online_resource_from_file(abs_path):
        with open(abs_path, "r") as f:
            return json.load(f)

    def get_online_problems(category, offline):
        root_path = get_root_path()
        abs_file_path = os.path.join(
            root_path, "others", f"api-cn.{category}.backup.json")
        if offline:
            obj = load_online_resource_from_file(abs_file_path)
            return obj
        obj = client.getJson(
            f"https://leetcode-cn.com/api/problems/{category}/")
        # LeetCode removed one question
        ADDITIONAL_QUESTIONS = [
            {'stat': {'question__title': '简单游戏', 'question__title_slug': '1zD30O',
                      'question__hide': False, 'frontend_question_id': 'DD-2020006'},
             'difficulty': {'level': 1},
             'paid_only': False},
            {'stat': {'question__title': 'Bulb Switcher III', 'question__title_slug': 'bulb-switcher-iii',
                      'question__hide': False, 'frontend_question_id': '1375'},
             'difficulty': {'level': 2},
             'paid_only': False},
            {'stat': {'question__title': 'Minimum Deletion Cost to Avoid Repeating Letters', 'question__title_slug': 'minimum-deletion-cost-to-avoid-repeating-letters',
                      'question__hide': False, 'frontend_question_id': '1578'},
             'difficulty': {'level': 2},
             'paid_only': False}
        ]
        for additional_question in ADDITIONAL_QUESTIONS:
            if not any(q['stat']['question__title_slug'] == additional_question['stat']['question__title_slug'] for q in obj["stat_status_pairs"]):
                obj["stat_status_pairs"].append(additional_question)
            else:
                print("The question is added in online list: " + str(additional_question))
        save_online_resource(obj, abs_file_path)
        return obj

    def list_code_folders():
        folder_patterns = ["\d{4}-\d{4}", "LCS",
                           "LCP", "剑指 Offer II", "剑指 Offer", "面试题", "DD"]
        folder_pattern = "^((" + ")|(".join(folder_patterns) + "))$"
        folder_matcher = re.compile(folder_pattern)
        root_path = get_root_path()
        return [os.path.join(root_path, folder) for folder in os.listdir(root_path) if folder_matcher.match(folder)]

    def list_local_solutions():
        folders = list_code_folders()
        solutions = []
        for folder in folders:
            for file_name in os.listdir(folder):
                solutions.append(Solution(os.path.join(folder, file_name)))
        root_path = get_root_path()
        known_children_patterns = [
            "\d{4}-\d{4}", "LCS", "LCP", "剑指 Offer II", "剑指 Offer", "面试题", "DD", ".git", ".gitignore", "others", ".DS_Store", README_FILENAME]
        known_children_pattern = "^((" + \
            ")|(".join(known_children_patterns) + "))$"
        known_children_matcher = re.compile(known_children_pattern)
        for file_name in os.listdir(root_path):
            if not known_children_matcher.match(file_name):
                solutions.append(Solution(os.path.join(root_path, file_name)))
        return solutions

    global DB_PROBLEMS
    questions = list(sorted([Question(prob) for prob in get_online_problems('all', offline)[
                     "stat_status_pairs"]], key=lambda q: q.order()))
    if not DB_PROBLEMS:
        DB_PROBLEMS = {item['stat']['frontend_question_id']
                       for item in get_online_problems('database', offline)["stat_status_pairs"]}
    ONLINE_MAP.update({q.id(): q for q in questions})
    solutions = list_local_solutions()
    for sol in solutions:
        LOCAL_MAP[sol.id()].append(sol)
    return questions, solutions

# ======== correct local files ========


def correct_local_files(questions, solutions):
    try:
        for sol in solutions:
            if sol.is_misplaced():
                sol.correct_location()
    finally:
        print()
        print("%d file(s) moved." % Solution.moved_cnt)


# ======== search solutions ========
def search_local_solutions(qid):
    if qid.isdigit():
        qid = str(int(qid))
    if qid in ATTEMPTED:
        print(qid + " was attempted.")
    elif qid in NOT_BACKFILLED:
        print(qid + " was completed, but not submitted to GitHub.")
    elif LOCAL_MAP[qid]:
        for sol in LOCAL_MAP[qid]:
            print(sol.original_abs_path())
    else:
        print("Not found")

# ======== generate subtables ========


def select_todo_without_lock(qid):
    if qid in NOT_BACKFILLED:
        return False
    if len(LOCAL_MAP[qid]):
        return False
    if ONLINE_MAP[qid].lock():
        return False
    return True


def filter_questions_and_solutions(questions, solutions, selector):
    rtn_questions = [
        question for question in questions if selector(question.id())]
    rtn_solutions = [
        solution for solution in solutions if selector(solution.id())]
    return rtn_questions, rtn_solutions


# ======== main ========

def main():
    client = Client()
    argv = list(sys.argv)
    offline = "offline" in argv
    if offline:
        argv.remove("offline")
    questions, solutions = load_resources(client, offline)

    if len(argv) == 1:
        correct_local_files(questions, solutions)
        all_questions = sorted([sol.mock_question_for_unrecognized_contest_solution(
        ) for sol in UNRECOGNIZED_CONTEST_SOLUTIONS.values()], key=lambda q: q.id(), reverse=True) + questions
        markdown = gen_markdown(
            all_questions, solutions, "My LeetCode solutions", MarkdownType.MAIN_README)
        update_file(README_FILENAME, markdown)

        all_questions = sorted([sol.mock_question_for_unrecognized_contest_solution(
        ) for sol in UNRECOGNIZED_CONTEST_SOLUTIONS.values()], key=lambda q: q.id(), reverse=True) + questions
        markdown = gen_markdown(all_questions, solutions,
                                "My LeetCode solutions", MarkdownType.FULL_TABLE)
        update_file(os.path.join("others", all_items_file_name), markdown)

        todo_que, todo_sol = filter_questions_and_solutions(
            questions, solutions, select_todo_without_lock)
        markdown = gen_markdown(
            todo_que, todo_sol, "To do questions", MarkdownType.TODO_PROBS)
        update_file(os.path.join("others", "todo questions.md"), markdown)
    elif len(argv) == 2:
        search_local_solutions(argv[1])
    else:
        raise Exception("Too many arguments.")


if __name__ == "__main__":
    main()
    # fetch discussions only when needed
    # TopicManager("kaiwensun", 50).generate_local_files()
