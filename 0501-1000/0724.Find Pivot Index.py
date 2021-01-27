class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sm = sum(nums)
        prefix = 0
        for i in xrange(len(nums)):
            if prefix == sm - prefix - nums[i]:
                return i
            prefix += nums[i]
        return -1

