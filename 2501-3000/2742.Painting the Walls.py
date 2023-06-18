from functools import cache

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        walls = sorted(zip(cost, time), key=lambda item: -item[1])
        @cache
        def dp(i, painted):
            if painted >= len(walls):
                return 0
            if i == len(walls):
                return float("inf")
            c, t = walls[i]
            return min(
                dp(i + 1, painted),
                dp(i + 1, painted + 1 + t) + c
            )

        return dp(0, 0)

