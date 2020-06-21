class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = list(start + 2 * i for i in xrange(n))
        res = 0
        for num in nums:
            res ^= num
        return res
