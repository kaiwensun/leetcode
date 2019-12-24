import collections
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        T = lambda: collections.defaultdict(T)
        words = sorted(words, key=len)
        trie = T()
        res = []
        for word in words:
            if word:
                p = trie
                for c in word:
                    p = p[c]
                p["#"] = word
            
        def dfs(p, word, i):
            if i == len(word):
                return "#" in p and p["#"] != word
            if "#" in p and dfs(trie, word, i):
                return True
            c = word[i]
            if c in p and dfs(p[c], word, i + 1):
                return True
            return False
        res = []
        for word in words:
            if dfs(trie, word, 0):
                res.append(word)
        return res
