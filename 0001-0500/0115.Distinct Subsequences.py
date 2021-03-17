from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i == len(s) or j == len(t):
                return int(j == len(t))
            res = dp(i + 1, j)
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            return res
        return dp(0, 0)

