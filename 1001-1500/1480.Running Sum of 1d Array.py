class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
