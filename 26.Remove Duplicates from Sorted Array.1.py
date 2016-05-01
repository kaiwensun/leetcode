class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l=l+1
        return l
