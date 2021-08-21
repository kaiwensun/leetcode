# This is not the optiomal solution

from functools import cache

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        blocks.sort()
        @cache
        def dp(start, end):
            if start + 1 == end:
                return blocks[start]
            l, r = start + 1, end
            res = float("inf")
            while l < r:
                mid = (l + r) // 2
                if dp(start, mid) < dp(mid, end):
                    l = mid + 1
                else:
                    r = mid
                res = min(res, max(dp(start, mid), dp(mid, end)))
            return res + split

        return dp(0, len(blocks))

