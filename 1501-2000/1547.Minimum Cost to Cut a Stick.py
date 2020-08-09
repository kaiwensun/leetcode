from functools import lru_cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = list(sorted([0] + cuts + [n]))
        @lru_cache(None)
        def calcCost(cut_l, cut_r):
            if cut_l + 1 == cut_r:
                return 0
            res = float('inf')
            for cut_i in range(cut_l + 1, cut_r):
                res = min(res, calcCost(cut_l, cut_i) + calcCost(cut_i, cut_r))
            return cuts[cut_r] - cuts[cut_l] + res
        return calcCost(0, len(cuts) - 1)

