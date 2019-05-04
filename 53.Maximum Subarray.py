class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = pre = 0
        for n in nums:
            pre = max(pre + n, 0)
            res = max(res, pre)
        if res == 0:
            return max(nums)
        return res
