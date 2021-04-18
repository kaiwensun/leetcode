class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(1, len(nums)):
            res += max(0, nums[i - 1] + 1 - nums[i])
            nums[i] = max(nums[i], nums[i - 1] + 1)
        return res

