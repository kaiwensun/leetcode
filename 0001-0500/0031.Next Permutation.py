u"""
Basic Idea:
	i从末尾向左扫描nums，数字nums[i]逐渐增大（非递减）……突然，不再非递减序列了，这时候我们就知道，如果把这个导致不再非递减的数nums[i]稍稍变大一点，然后把其右侧的数从小到大排列，那么得到的就是我们要求的下一个排列。
	怎么“稍稍变大一点”呢？就是在i右侧找到严格比nums[i]大的数中最小的那个数。把它与nums[i]交换。
	几个小的优化点：
	1.调用findleastid(nums,startfrom,greaterthan)的时候，利用好“startfrom右侧是个非递增序列”这一特点，尽早break。（进一步可用二分查找，本代码未实现）
	2.如果整个nums是最大序列，那我们在重新把nums的元素由小到大排序时可以利用好“nums是个非递增序列”这一特点，直接nums.reverse()，而不是用nums.sort()
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return nums
        biggest = nums[-1]
        for i in xrange(len(nums)-2,-1,-1):
            if nums[i]<biggest:
                leastid = self.findleastid(nums,i+1,nums[i])
                tmp = nums[i]
                nums[i]=nums[leastid]
                nums[leastid]=tmp
                self.myqsort(nums,i+1,len(nums)-1)
                return
            else:
                biggest=nums[i]
        nums.reverse()
    
    def findleastid(self,nums,startfrom,greaterthan):
        leastid=startfrom
        for i in xrange(startfrom+1,len(nums)):
            if nums[leastid]>nums[i] and nums[i]>greaterthan:
                leastid=i
            elif nums[leastid]<nums[i]:
                break
        return leastid
            
    def myqsort(self,nums,left,right):
        if left>=right:
            return nums
        pivot = nums[right]
        l,r=left,right
        while l<r:
            if nums[l]<pivot:
                l=l+1
            else:
                nums[r]=nums[l]
                r=r-1
                nums[l]=nums[r]
        nums[l]=pivot
        self.myqsort(nums,left,l-1)
        self.myqsort(nums,l+1,right)

