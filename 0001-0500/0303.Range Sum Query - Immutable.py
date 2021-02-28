class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in xrange(len(nums) - 1):
            nums[i + 1] += nums[i]
        nums.append(0)
        self.prefix = nums


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix[j] - self.prefix[i - 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

