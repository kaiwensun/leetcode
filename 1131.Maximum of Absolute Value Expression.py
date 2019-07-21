class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        n = len(arr1)
        A = [arr1[i] + arr2[i] + i for i in xrange(n)]
        B = [arr1[i] + arr2[i] - i for i in xrange(n)]
        C = [arr1[i] - arr2[i] + i for i in xrange(n)]
        D = [arr1[i] - arr2[i] - i for i in xrange(n)]
        return max(max(arr) - min(arr) for arr in (A, B, C, D))
