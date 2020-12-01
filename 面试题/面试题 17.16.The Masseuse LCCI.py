class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        take = no_take = 0
        for num in nums:
            take, no_take = no_take + num, max(take, no_take)
        return max(take, no_take)

