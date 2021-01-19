import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallests = heapq.nsmallest(2, nums)
        biggest = heapq.nlargest(3, nums)
        return max(smallests[0] * smallests[1] * biggest[0], biggest[0] * biggest[1] * biggest[2])

