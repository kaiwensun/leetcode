class Solution(object):
    def clumsy(self, N, op='-'):
        """
        :type N: int
        :rtype: int
        """
        if N <= 4:
            if N == 1:
                return 1
            if N == 2:
                return 2
            if N == 3:
                return 6
        rval = N * (N - 1) / (N - 2)
        for n in xrange(N - 3, 0, -4):
            rval += self.calcFour(n)
        return rval

    def calcFour(self, N):
        if N <= 4:
            return -2 if N == 4 else 1
        else:
            return N - (N - 1) * (N - 2) / (N - 3)
