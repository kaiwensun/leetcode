import collections
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        def dfs(p, word, i):
            if i == len(word):
                return "#" in p
            if "#" in p and dfs(trie, word, i):
                return True
            c = word[i]
            if c in p and dfs(p[c], word, i + 1):
                return True
            return False

        T = lambda: collections.defaultdict(T)
        trie = T()
        res = []
        words.sort(key=len)
        for word in words:
            if not word:
                continue
            if dfs(trie, word, 0):
                res.append(word)
            else:
                p = trie
                for c in word:
                    p = p[c]
                p["#"] = True
        return res

