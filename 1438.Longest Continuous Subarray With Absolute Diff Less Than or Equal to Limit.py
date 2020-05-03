import heapq
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_heap = [(float('inf'), len(nums))]
        max_left = -1
        min_heap = [(float('inf'), len(nums))]
        min_left = -1
        res = 0
        for i, num in enumerate(nums):
            while -max_heap[0][0] > num + limit or max_heap[0][1] < max_left:
                max_left = max(max_left, max_heap[0][1])
                heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-num, i))
            while min_heap[0][0] < num - limit or min_heap[0][1] < min_left:
                min_left = max(min_left, min_heap[0][1])
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, (num, i))
            res = max(res, i - max(max_left, min_left))
        return res
