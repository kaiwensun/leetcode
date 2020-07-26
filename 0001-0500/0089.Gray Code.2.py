class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(n):
            res = [ele << 1 for ele in res] + [(ele << 1) | 1  for ele in reversed(res)]
        return res
