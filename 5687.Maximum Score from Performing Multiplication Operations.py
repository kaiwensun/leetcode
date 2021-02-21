import functools
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        @functools.lru_cache(None)
        def dp(start, i):
            end = len(nums) - 1 - i + start
            if i == len(multipliers) - 1:
                return max(multipliers[i] * nums[start], multipliers[i] * nums[end])
            return max(multipliers[i] * nums[start] + dp(start + 1, i + 1),
                       multipliers[i] * nums[end] + dp(start, i + 1))
        res = dp(0, 0)
        dp.cache_clear()
        return res

