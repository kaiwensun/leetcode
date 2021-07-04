class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [nums[nums[i]] for i in xrange(len(nums))]

