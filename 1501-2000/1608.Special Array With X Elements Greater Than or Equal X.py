class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        last = -1
        for i, num in enumerate(nums):
            if num >= len(nums) - i and last < len(nums) - i:
                return len(nums) - i
            last = num
        return -1

