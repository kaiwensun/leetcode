class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=0
        r=0
        while r<len(nums):
            while r<len(nums):
                if nums[r]==0:
                    r=r+1
                else:
                    break
            else:
                break
            nums[l]=nums[r]
            l=l+1
            r=r+1
        while l<len(nums):
            nums[l]=0
            l=l+1
        

