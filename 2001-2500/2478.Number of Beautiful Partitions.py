from functools import cache
from bisect import bisect_left

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        minLength = max(2, minLength)
        primes = set("2357")
        if s[0] not in primes or s[-1] in primes:
            return 0
        MOD = 10 ** 9 + 7
        
        start_points = []
        for i in range(1, len(s) - 1):
            if s[i] in primes and s[i - 1] not in primes:
                start_points.append(i)
        start_points.append(len(s))

        @cache
        def dp(start_index, prev_substr_cnt):
            if start + minLength * (k - prev_substr_cnt) > len(s):
                return 0
            if start == len(s):
                return 1 if prev_substr_cnt == k else 0
            if prev_substr_cnt > k:
                return 0
            res = 0
            min_start_index = start + minLength
            j = bisect_left(start_points, min_start_index)
            for next_start_index in range(j, len(start_points)):
                next_start = start_points[next_start_index]
                res += dp(next_start, prev_substr_cnt + 1)
            return res % MOD
        return dp(0, 0)

