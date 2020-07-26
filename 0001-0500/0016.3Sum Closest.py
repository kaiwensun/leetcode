#import pdb
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        print nums
        diff = 2**30
        rtn=0
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                tmp_diff = (target-nums[i]-nums[l]-nums[r])
                if abs(tmp_diff)<diff:
#                    if nums[r]==-18:
#                        pdb.set_trace()
                    diff = abs(tmp_diff)
                    rtn = target-tmp_diff
                    print '%d,%d,%d,%d,%d,%d\n'%(nums[i],nums[l],nums[r],i,l,r)
                if diff==0:
                    return target
                elif tmp_diff>0:
                    l=l+1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
                else:
                    r=r-1
                    while l<r and nums[r]==nums[r+1]:
                        r=r-1
        return rtn
                

s = Solution()
L = [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
T = -59
print s.threeSumClosest(L,T)
