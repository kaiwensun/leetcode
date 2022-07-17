import heapq
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            return sum(map(int, str(num)))
        d = defaultdict(list)
        for num in nums:
            d[digit_sum(num)].append(num)
        res = -1
        for values in d.values():
            if len(values) >= 2:
                res = max(res, sum(nlargest(2, values)))
        return res

