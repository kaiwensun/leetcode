from functools import cache

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        @cache
        def dp(i, prev):
            if i == len(nums):
                return 0
            if nums[i] >= k:
                return dp(i + 1, i)
            res = k - nums[i] + dp(i + 1, i)
            if i - prev < 3:
                res = min(res, dp(i + 1, prev))
            return res
        return dp(0, -1)

