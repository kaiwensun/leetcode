from functools import cache

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i):
            if i == n:
                return True
            if i + 1 < n and nums[i] == nums[i + 1] and dp(i + 2):
                return True
            if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2] and dp(i + 3):
                return True
            if i + 2 < n and nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2 and dp(i + 3):
                return True
            return False
        return dp(0)

