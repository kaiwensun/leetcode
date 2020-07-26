class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in xrange(n):
            res.append(nums[i])
            res.append(nums[n + i])
        return res
