from collections import Counter
from functools import cache

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = list(Counter(nums).values())
        
        @cache
        def dp(i, rem):
            if i == len(cnt):
                return 1 if rem == 0 else 0
            if rem == 0:
                return 1
            return cnt[i] * dp(i + 1, rem - 1) + dp(i + 1, rem)
        return dp(0, 3)

