class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn, mx = nums[0], nums[0]
        res = max(mn, mx)
        for num in nums[1:]:
            prods = (mn * num, mx * num, num)
            mn, mx = min(prods), max(prods)
            res = max(res, mn, mx)
        return res

