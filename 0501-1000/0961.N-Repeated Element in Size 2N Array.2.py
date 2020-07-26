class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in xrange(1, len(A)):
            if A[i - 1] == A[i]:
                return A[i]
        if A[0] in A[-2:]:
            return A[0]
        return A[1]
