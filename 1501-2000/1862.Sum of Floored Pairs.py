from collections import Counter
from bisect import bisect_left

MOD = 10 ** 9 + 7
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        num_cnts = list(sorted(Counter(nums).items()))
        suffix_sum = [0] * (len(num_cnts) + 1)
        for i in range(len(num_cnts) - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + num_cnts[i][1]
        res = 0
        for i in range(len(num_cnts)):
            target = num_cnts[i][0]
            start = i
            target_res = 0
            times = 1
            while start < len(num_cnts):
                target_res += suffix_sum[start]
                target += num_cnts[i][0]
                start = bisect_left(num_cnts, (target, -1), lo=start)
            res += target_res * num_cnts[i][1]
        return res % MOD

