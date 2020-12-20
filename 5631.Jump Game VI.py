import heapq
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        queue = [(-nums[0], 0)]  # (sum, index)
        res = []
        for i in xrange(1, len(nums)):
            while queue[0][1] < i - k:
                heapq.heappop(queue)
            if i == len(nums) - 1:
                return -queue[0][0] + nums[i]
            heapq.heappush(queue, (queue[0][0] - nums[i], i))
        return nums[0]

