from functools import cache
from bisect import bisect_left

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()

        @cache
        def dp(start):
            i = bisect_left(offers, [start, -1, -1])
            if i == len(offers):
                return 0
            res = dp(start + 1)
            for j in range(i, len(offers)):
                offer = offers[j]
                if offer[0] != start:
                    break
                res = max(res, offer[2] + dp(offer[1] + 1))
            return res
        return dp(0)

