class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        l = 0
        r = len(nums)-1
        while(l<r):
            if nums[l]==val:
                nums[l]=nums[r]
                r=r-1
            else:
                l = l+1
        if nums[l]!=val:
            l=l+1
        return l
        

