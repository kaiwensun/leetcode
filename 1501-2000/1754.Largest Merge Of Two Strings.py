from functools import lru_cache

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        @lru_cache(None)
        def dp(i, j):
            if i == len(word1):
                return 1
            if j == len(word2):
                return 0
            if word1[i] != word2[j]:
                return 0 if word1[i] > word2[j] else 1
            return dp(i + 1, j + 1)

        pointers = [0, 0]
        words = [word1, word2]
        res = []
        for k in range(len(word1) + len(word2)):
            p = dp(*pointers)
            res.append(words[p][pointers[p]])
            pointers[p] += 1
        return "".join(res)

