class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        size = len(nums) + max(map(len, nums))
        buckets = [[] for _ in xrange(size)]
        for i in xrange(len(nums)):
            for j in xrange(len(nums[i])):
                buckets[i + j].append(nums[i][j])
        res = []
        for bucket in buckets:
            res.extend(reversed(bucket))
        return res
