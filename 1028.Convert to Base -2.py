class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        rval = ''
        while N != 0:
            remainder = -N % 2
            N = (N - remainder) / -2
            rval = str(remainder) + rval
        return rval if rval else '0'
