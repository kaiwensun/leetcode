from functools import cache

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        @cache
        def dp(used_bits, prev):
            if used_bits == (1 << n) - 1:
                return abs(prev - nums[0]), []
            mn = float("inf")
            mn_list = None
            for nxt in range(n):
                if (1 << nxt) & used_bits:
                    continue
                tail_mn, tail_mn_list = dp(used_bits | (1 << nxt), nxt)
                if abs(prev - nums[nxt]) + tail_mn < mn:
                    mn = abs(prev - nums[nxt]) + tail_mn
                    mn_list = [nxt] + tail_mn_list
            return mn, mn_list
        return [0] + dp(1, 0)[1]

