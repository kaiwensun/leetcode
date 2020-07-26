"""
Your runtime beats 60.19% of python submissions.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=map(lambda x:0 if x<=0 or x>len(nums) else x,nums)
        m = len(nums)+1
        for x in xrange(len(nums)):
            if nums[x]<=0:
                continue
            else:
                nums[nums[x]%m-1]=nums[nums[x]%m-1]%m+m
        for x in xrange(len(nums)):
            if nums[x]<=len(nums):
                return x+1
        return len(nums)+1
                

