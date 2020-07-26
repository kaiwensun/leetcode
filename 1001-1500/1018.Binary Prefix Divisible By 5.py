class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        rval = [None] * len(A)
        n = 0
        for i, a in enumerate(A):
            n = ((n << 1) + a) % 5
            rval[i] = n == 0
        return rval
