import functools
class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(index, prev_robbed, first_robbed):
            if index >= len(nums):
                return 0
            if index == 0:
                if first_robbed:
                    return nums[index] + dp(index + 1, True, first_robbed)
                else:
                    return dp(index + 1, False, first_robbed)
            if index == len(nums) - 1:
                if first_robbed or prev_robbed:
                    return 0
                else:
                    return nums[index]
            if prev_robbed:
                return dp(index + 1, False, first_robbed)
            return max(
                nums[index] + dp(index + 1, True, first_robbed),
                dp(index + 1, False, first_robbed)
            )
        return max(dp(0, True, False), dp(0, False, True), dp(0, False, False))
