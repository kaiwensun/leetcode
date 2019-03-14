class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while j < len(nums):
            if i < 2 or nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
