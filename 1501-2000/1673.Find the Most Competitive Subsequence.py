import heapq
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        heap = []
        for i in xrange(len(nums) - k):
            heapq.heappush(heap, (nums[i], i))
        selected = -1
        for i in xrange(len(nums) - k, len(nums)):
            heapq.heappush(heap, (nums[i], i))
            while heap[0][1] < selected:
                heapq.heappop(heap)
            num, selected = heapq.heappop(heap)
            res.append(num)
        return res

