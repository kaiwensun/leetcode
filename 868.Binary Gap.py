class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        last = None
        for i in xrange(30):
            if N & 1:
                res = res if last is None else max(res, i - last)
                last = i
            N >>= 1
        return res
