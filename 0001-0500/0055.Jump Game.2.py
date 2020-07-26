class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reached = 0
        for i in xrange(len(nums)):
            if i > reached:
                return reached >= len(nums) - 1
            reached = max(reached, i + nums[i])
        return True
