class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = left = right = 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            right += 1
            while product >= k and left < right:
                product /= nums[left]
                left += 1
            res += right - left
        return res
