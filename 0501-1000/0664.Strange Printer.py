from functools import lru_cache

class Solution:
    def strangePrinter(self, s: str) -> int:

        @lru_cache(None)
        def dp(start, end):
            if start + 1 == end:
                return 1
            if lst[start] == lst[end - 1]:
                return dp(start, end - 1)
            return min(dp(start, mid) + dp(mid, end) for mid in range(start + 1, end))

        lst = [s[0]]
        i = 0
        for j in range(len(s)):
            if s[j] != lst[-1]:
                lst.append(s[j])
        return dp(0, len(lst))

