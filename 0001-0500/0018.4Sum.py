class Solution(object):
    #List = []
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.List = []
        nums.sort()
        if len(nums)<4 or nums[0]*4>target or nums[-1]*4<target:
            return self.List
        i=0
        while i < len(nums)-3:
            self.threeSum(nums[i+1:len(nums)],target-nums[i],nums[i])
            while i+1<len(nums)-3 and nums[i]==nums[i+1]:
                i=i+1
            i=i+1
        return self.List
    
    
    def threeSum(self,nums,target,a):
        if nums[0]*3>target or nums[-1]*3<target:
            return
        i=0
        while i < len(nums)-2:
            self.twoSum(nums[i+1:len(nums)],target-nums[i],a,nums[i])
            while i+1<len(nums)-2 and nums[i]==nums[i+1]:
                i=i+1
            i=i+1
    
    def twoSum(self,nums,target,a,b):
        if nums[0]*2>target or nums[-1]*2<target:
            return
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l]*2>target:
                return True
            if nums[r]*2<target:
                return True
            sumation = nums[l]+nums[r]
            if sumation==target:
                self.List.append([a,b,nums[l],nums[r]])
                l=l+1
                while l<r and nums[l-1]==nums[l]:
                    l=l+1
                r=r-1
                while l<r and nums[r]==nums[r+1]:
                    r=r-1
            elif sumation>target:
                r = r-1
                while l<r and nums[r]==nums[r+1]:
                    r=r-1
            else:
                l=l+1
                while l<r and nums[l-1]==nums[l]:
                    l=l+1


lst = [-5,5,4,-3,0,0,4,-2]
target = 4
s = Solution()
print s.fourSum(lst,target)

