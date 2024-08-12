from functools import cache
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        @cache
        def cost(x1, y1, x2, y2):
            if x1 + 1 == x2 and y1 + 1 == y2:
                return 0
            res = float("inf")
            for x in range(x1 + 1, x2):
                res = min(res, verticalCut[x] + cost(x1, y1, x, y2) + cost(x, y1, x2, y2))
            for y in range(y1 + 1, y2):
                res = min(res, horizontalCut[y] + cost(x1, y, x2, y2) + cost(x1, y1, x2, y))
            return res
        return cost(-1, -1, n - 1, m - 1)

