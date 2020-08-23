from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(len(stoneValue) + 1)
        def prefix(i):
            if i == -1:
                return 0
            return prefix(i - 1) + stoneValue[i]
        
        def sum_range(i, j):
            return prefix(j - 1) - prefix(i - 1)

        @lru_cache(None)
        def dp(i, j):
            if i + 1 == j:
                return 0
            res = 0
            for split in range(i + 1, j):
                left_sm = sum_range(i, split)
                right_sm = sum_range(split, j)
                if left_sm >= right_sm:
                    res = max(res, right_sm + dp(split, j))
                if left_sm <= right_sm:
                    res = max(res, left_sm + dp(i, split))
            return res
        return dp(0, len(stoneValue))

