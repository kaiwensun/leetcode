from functools import lru_cache

class Solution:
    def minCut(self, s: str) -> int:
        palindromes = [[] for _ in range(len(s))]
        def find_palindromes(i, j):
            while 0 <= i <= j < len(s) and s[i] == s[j]:
                palindromes[i].append(j + 1)
                i -= 1
                j += 1

        @lru_cache(None)
        def cost(i):
            if i == len(s):
                return 0
            return 1 + min(cost(nxt) for nxt in palindromes[i]) if palindromes[i] else float("inf")

        for i in range(len(s)):
            find_palindromes(i, i)
            find_palindromes(i, i + 1)
        return cost(0) - 1

