import functools
class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i <= 1: return 0
            return dp(i + 1, j - 1) if s[i] == s[j - 1] else min(dp(i + 1, j) + 1, dp(i, j - 1) + 1)
        return dp(0, len(s))
