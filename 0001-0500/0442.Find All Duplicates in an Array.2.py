class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            slot = abs(num) - 1
            seen = nums[slot] < 0
            if seen:
                res.append(abs(num))
            nums[slot] = -nums[slot] 
        return res
