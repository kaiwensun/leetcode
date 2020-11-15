class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        expected = sum(nums) - x
        l = r = 0
        sm = 0
        res = float("inf")
        while True:
            if sm == expected:
                res = min(res, len(nums) - r + l)
            if sm <= expected:
                if r >= len(nums):
                    break
                sm += nums[r]
                r += 1
            else:
                if l >= len(nums):
                    break
                sm -= nums[l]
                l += 1
        return res if res <= len(nums) else -1

