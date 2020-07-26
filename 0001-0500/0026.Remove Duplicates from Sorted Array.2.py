import pdb
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        l=1
        r=0
        while r<len(nums):
            step = (len(nums)-r)/2
            if step==0:
                break
            while r+step>=len(nums) or nums[r+step]>nums[r]:
                step=step/2
            old_r = r
            r=r+max(step,1)
            if nums[r]!=nums[old_r]:
                nums[l]=nums[r]
                l=l+1
        return l

            
l = [1,1,2]        
s=Solution()
pdb.set_trace()
print s.removeDuplicates(l)
print l
