class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        sortedPtr = 0
        lookFor = 0
        lookForPtr = 0
        while sortedPtr < len(nums):
            while lookForPtr < len(nums) and nums[lookForPtr] != lookFor:
                lookForPtr += 1
            if lookForPtr == len(nums):
                lookFor += 1
                lookForPtr = sortedPtr
            else:
                nums[sortedPtr], nums[lookForPtr] = nums[lookForPtr], nums[sortedPtr]
                sortedPtr += 1
                lookForPtr += 1
