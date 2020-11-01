from functools import lru_cache
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dp(i, j, diff_was_used):
            if i >= len(s) or j >= len(t):
                return 0
            if diff_was_used:
                if s[i] == t[j]:
                    res = 1 + dp(i + 1, j + 1, diff_was_used)
                else:
                    res = 0
            else:
                if s[i] == t[j]:
                    res = dp(i + 1, j + 1, diff_was_used)
                else:
                    res = 1 + dp(i + 1, j + 1, True)
            return res

        return sum(dp(i, j, False) for i in range(len(s)) for j in range(len(t)))

