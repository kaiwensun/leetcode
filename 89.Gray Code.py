class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(n):
            res += [(1 << i) | ele for ele in reversed(res)]
        return res
