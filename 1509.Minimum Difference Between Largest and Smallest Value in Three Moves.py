import heapq
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 4:
            return 0
        largest = heapq.nlargest(4, nums)
        smallest = heapq.nsmallest(4, nums)
        return min(largest[i] - smallest[3 - i] for i in xrange(4))
