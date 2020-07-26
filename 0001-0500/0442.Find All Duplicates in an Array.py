class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res
