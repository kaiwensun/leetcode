class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        N = 1
        rval = 1
        if K % 10 not in [1,3,9,7]:
            return -1
        seen = set()
        while True:
            if N in seen:
                return -1
            if N % K == 0:
                return rval
            seen.add(N)
            N = (N * 10 + 1) % K
            rval += 1
