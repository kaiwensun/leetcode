class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums))<3:
            return []
        nums.sort()
        rtn = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            l=i+1
            r=len(nums)-1
            while(l<r):
                if nums[l]+nums[r]==target:
                    rtn.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l=l+1
                    r=r-1
                    while r>=0 and nums[r]==nums[r+1]:
                        r=r-1
                elif nums[l]+nums[r]<target:
                    l=l+1
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l=l+1
                else:
                    r=r-1
                    while r>=0 and nums[r]==nums[r+1]:
                        r=r-1
        return rtn