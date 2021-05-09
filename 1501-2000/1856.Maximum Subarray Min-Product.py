import heapq
from sortedcontainers import SortedList

MOD = 10 ** 9 + 7

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        def get_range_sum(start, end):
            return prefix_sum[end] - prefix_sum[start]
        
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        heap = [tuple(reversed(pair)) for pair in enumerate(nums)]
        heapq.heapify(heap)
        intervals = SortedList([(0, len(nums))])
        res = 0
        while heap:
            mn_num, mn_num_index = heapq.heappop(heap)
            interval_index = intervals.bisect_right((mn_num_index, float("inf"))) - 1
            start, end = intervals[interval_index]
            res = max(res, get_range_sum(start, end) * mn_num)
            intervals.remove((start, end))
            if start < mn_num_index:
                intervals.add((start, mn_num_index))
            if mn_num_index + 1 < end:
                intervals.add((mn_num_index + 1, end))
        return res % MOD

