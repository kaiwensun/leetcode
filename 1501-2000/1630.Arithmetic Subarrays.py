class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def test(nums):
            if len(nums) <= 2:
                return True
            nums.sort()
            diff = nums[1] - nums[0]
            for i in xrange(2, len(nums)):
                if nums[i] - nums[i - 1] != diff:
                    return False
            return True
        return [test(nums[left : right + 1]) for left, right in zip(l, r)]

