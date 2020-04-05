class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums, reverse=True)
        sm = sum(nums)
        res_sum = 0
        res = []
        for a in nums:
            res_sum += a
            res.append(a)
            if res_sum > sm - res_sum:
                break
        return res
