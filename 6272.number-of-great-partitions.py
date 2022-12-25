from functools import cache

MOD = 10 ** 9 + 7
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * len(nums)
        for i in range(len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]
        if prefix_sum[-1] < k * 2:
            return 0

        @cache
        def dp(i, need1, need2):
            if i < 0 and max(need1, need2) > 0:
                return 0
            if max(need1, need2) > prefix_sum[i]:
                return 0
            if need1 == need2 == 0:
                return pow(2, (i + 1), MOD)
            if need1 > need2:
                return dp(i, need2, need1)
            return (dp(i - 1, max(0, need1 - nums[i]), need2) + dp(i - 1, need1, max(0, need2 - nums[i]))) % MOD

        return dp(len(nums) - 1, k, k)

