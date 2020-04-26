import heapq
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        res = float('-inf')
        for j, num in enumerate(nums):
            while heap and (heap[0][1] < j - k or -heap[0][0] <= 0):
                heapq.heappop(heap)
            new_sum = -heap[0][0] + num if heap else num
            res = max(res, new_sum)
            heapq.heappush(heap, (-new_sum, j))
        return res
