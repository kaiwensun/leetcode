from functools import cache
from collections import Counter

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        num2indexes = Counter()
        for i, num in enumerate(nums):
            num2indexes[num] |= 1 << i

        @cache
        def dp(i, avoid_bits):
            if i == len(nums):
                return 1
            num = nums[i]
            res = dp(i + 1, avoid_bits)
            if (1 << i) & avoid_bits == 0:
                res += dp(i + 1, avoid_bits | num2indexes[num + k] | num2indexes[num - k])
            return res
        return dp(0, 0) - 1

