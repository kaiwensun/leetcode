from functools import lru_cache
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        
        @lru_cache(None)
        def putInMiddle(start, end):
            if start == end:
                return 0
            if start + 1 == end:
                return houses[end] - houses[start]
            return houses[end] - houses[start] + putInMiddle(start + 1, end - 1)
            
        @lru_cache(None)
        def dp(last_house, k):
            if last_house < k:
                return 0
            if k == 1:
                return putInMiddle(0, last_house)
            res = float("inf")
            for left_last_house in range(last_house):
                res = min(res, dp(left_last_house, k - 1) + putInMiddle(left_last_house + 1, last_house))
            return res
        houses.sort()
        return dp(len(houses) - 1, k)
