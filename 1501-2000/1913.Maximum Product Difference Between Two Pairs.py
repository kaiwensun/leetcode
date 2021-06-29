import heapq

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int.__mul__(*heapq.nlargest(2, nums)) - int.__mul__(*heapq.nsmallest(2, nums))

