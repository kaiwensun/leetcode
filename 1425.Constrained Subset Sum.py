import heapq
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx = max(nums)
        if mx <= 0:
            return mx
        heap = []
        res = 0
        for j, num in enumerate(nums):
            
            while heap and (heap[0][1] < j - k or -heap[0][0] <= 0):
                heapq.heappop(heap)
            if heap:
                new_sum = -heap[0][0] + num
            else:
                new_sum = num
            res = max(res, new_sum)
            heapq.heappush(heap, (-new_sum, j))
        return res
