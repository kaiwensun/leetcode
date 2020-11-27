from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(i, sm):
            if i == len(nums):
                return sm << 1 == total_sum
            if sm << 1 > total_sum:
                return False
            return dp(i + 1, sm) or dp(i + 1, sm + nums[i])

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        return dp(0, 0)

