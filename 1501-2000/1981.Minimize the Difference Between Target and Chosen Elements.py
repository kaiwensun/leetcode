from functools import cache

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        @cache
        def dp(i, sm):
            if i == len(mat):
                return abs(sm - target)
            res = float("inf")
            for num in mat[i]:
                res = min(res, dp(i + 1, sm + num))
                if res == 0:
                    break
            return res
        mat = list(map(set, mat))
        res = dp(0, 0)
        dp.cache_clear()
        return res

