class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        half = (len(nums) + 1) / 2
        nums[::2], nums[1::2] = nums[-half:], nums[:-half]
        return nums
