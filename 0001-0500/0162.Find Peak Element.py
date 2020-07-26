class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            left = nums[i - 1] if i != 0 else float('-inf')
            this = nums[i]
            right = nums[i + 1] if i != len(nums) - 1 else float('-inf')
            if left < this > right:
                return i
