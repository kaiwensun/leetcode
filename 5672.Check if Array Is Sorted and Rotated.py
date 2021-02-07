class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dropped = False
        for i in xrange(-1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if dropped:
                    return False
                dropped = True
        return True

