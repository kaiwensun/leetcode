#!/usr/bin/env python3

import functools
import os 
import re
import requests

class Question:
    
    """
    A class modeling online questions fetched from API
    """

    US_QUESTION_URL_PATTERN = "https://leetcode.com/problems/%s/"
    CN_QUESTION_URL_PATTERN = "https://leetcode-cn.com/problems/%s/"
    ONLINE_MAPPER = None

    def __init__(self, dic):
        self._id = str(dic["stat"]["frontend_question_id"])
        self._title = dic["stat"]["question__title"]
        if self._id == "1560":
            self._title = " ".join(self._title.split())
            
        self._lock = dic["paid_only"]
        self._difficulty = dic["difficulty"]["level"]
        self._slug = dic["stat"]["question__title_slug"]
        
    def is_us(self):
        return self._id.isdigit()

    def url(self):
        url_pattern = Question.US_QUESTION_URL_PATTERN if self.is_us() else Question.CN_QUESTION_URL_PATTERN
        return url_pattern % self._slug

    def id(self):
        return self._id

    def title(self):
        return self._title

    def order(self):
        if self.is_us():
            return (int(self.id()),)
        else:
            return (float("inf"), self.id())

    def __str__(self):
        return "%s, %s, %s" % (self.id(), self.title(), self.url())

class Solution:

    """
    A class modeling loca solution files"
    """

    FOLDER_SIZE = 500
    KNOWN_TYPES = {"c", "cpp", "java", "py", "rb", "sh", "js", "sql", "php", "txt"}
    KNOWN_CN_GROUPS = [
        re.compile("^LCP \d{2}$"),
        re.compile("^剑指 Offer \d{2}$"),
        re.compile("^面试题 \d{2}\.\d{2}$")
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
        rtn = self._basename.split(".")[-1]

    def id(self):
        if self.is_us():
            return str(int(self._id))
        else:
            return self._id
        
    def _parse_basename(self):
        # id.title[.version][.hint].typ
        splited = self._basename.split(".")
        if len(splited) > 5:
            raise ValueError("Unable to parse basename %s" % self._basename)
        for i in range(len(splited)):
            splited[i] = splited[i].strip()
            if not splited[i]:
                raise ValueError("Empty piece in file %s" % self._basename)
        self._typ = splited[-1]
        if self._typ not in Solution.KNOWN_TYPES:
            raise ValueError("Unknown file type for %s" % self._basename)
        self._id = splited[0]
        self._desired_folder = self._calc_desired_folder()
        self._title = self._version = self._hint = None
        for piece in splited[1:-1]:
            if piece.isdigit():
                if self._version is not None:
                    raise ValueError("Found multiple versions from basename %s" % self._basename)
                self._version = piece
            elif piece[0] == "(" and piece[-1] == ")":
                if self._hint is not None:
                    raise ValueError("Found multiple hints from basename %s" % self._basename)
                self._hint = piece[1:-1]
                if not self._hint:
                    raise ValueError("The hint in basename cannot be empty for %s" % self._basename)
            else:
                if self._title is not None:
                    raise ValueError("Found multiple titles from basename %s" % self._basename)
                self._title = piece
        question = Solution.ONLINE_MAPPER.get(self.id())
        if question is None:
            raise ValueError("Unable to auto-detect title from online source, for the basename %s", self._basename)
        if self._title is None:
            # tring to fill the title from online source
            print("[WARN] Solution %s name defaults to %s" % (self.id(), question.title()))
            self._title = question.title()
        else:
            if self._title != question.title():
                raise ValueError("file name doesn't match online question title: (online: %s, local: %s, basename: %s)" % (question.title(), self._title, self._basename))

    def is_us(self):
        return self._id.isdigit()

    def desired_folder(self):
        return self._desired_folder

    def _calc_desired_folder(self):
        if self.is_us():
            num = int(self._id)
            start = (num - 1) // Solution.FOLDER_SIZE * Solution.FOLDER_SIZE + 1
            end = start + Solution.FOLDER_SIZE - 1
            return "{:04d}-{:04d}".format(start, end)
        elif any(matcher.match(self._id) for matcher in Solution.KNOWN_CN_GROUPS):
            folders = ["LCP", "剑指 Offer", "面试题"]
            for folder in folders:
                if self._id.startswith(folder):
                    return folder
            else:
                raise Error("fail to assign a folder")
        else:
            raise ValueError("Unknown question id %s" % self._id)

    def desired_abs_path(self):
        return os.path.join(Solution.ROOT_PATH, self.desired_folder(), self.desired_basename())
        

    def is_misplaced(self):
        return self._abs_path != self.desired_abs_path()

    def correct_location(self):
        if os.path.exists(self.desired_abs_path()):
            raise Exception("Destination already exists: %s -> %s" % (self._abs_path, self.desired_abs_path()))
        print("Moving %s -> %s" % (self._abs_path, self.desired_abs_path()))
        Solution.moved_cnt += 1
        os.rename(self._abs_path, self.desired_abs_path())

    def desired_basename(self):
        res = ["{:04d}".format(int(self._id)) if self.is_us() else self._id,
            self._title]
        if self._version is not None:
            res.append(self._version)
        if self._hint is not None:
            res.append("(" + self._hint + ")")
        res.append(self._typ)
        return ".".join(res)

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
        
def list_code_folders():
    folder_patterns = ["\d{4}-\d{4}", "LCP", "剑指 Offer", "面试题"]
    folder_pattern = "^(" + ")|(".join(folder_patterns) + ")$"
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
    known_children_patterns = ["\d{4}-\d{4}", "LCP", "剑指 Offer", "面试题", "README.md", ".git", "others"]
    known_children_pattern = "^(" + ")|(".join(known_children_patterns) + ")$"
    known_children_matcher = re.compile(known_children_pattern)
    for file_name in os.listdir(root_path):
        if not known_children_matcher.match(file_name):
            solutions.append(Solution(os.path.join(root_path, file_name)))
    return solutions

def get_online_problems():
    return requests.get("https://leetcode-cn.com/api/problems/all/").json()

def get_root_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def move_files(problems):
    folder_pattern = "^\d{4}-\d{4}$"
    folder_matcher = re.compile(folder_pattern)
    root_path = get_root_path()
    excluded = ["others", ".git", "README.md"]
    files = [f for f in os.listdir(root_path) if not folder_matcher.match(f) and f not in excluded]

def main():
    questions = list(sorted([Question(prob) for prob in get_online_problems()["stat_status_pairs"]], key=lambda q:q.order()))
    question_mapper = {q.id() : q for q in questions}
    Solution.ONLINE_MAPPER = question_mapper
    for f in list_local_solutions():
        if f.is_misplaced():
            f.correct_location()
    print()
    print("%d file(s) moved." % Solution.moved_cnt)


if __name__ == "__main__":
    main()
# "\u5251\u6307 Offer 47".encode("utf-8").decode("utf-8")
