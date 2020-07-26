class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M, mayNeedSwap=True):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        lookLeft = [float('-inf')] * len(A)
        leftSum = sum(A[:L])
        lookLeft[L - 1] = sum(A[:L])
        for i in xrange(L, len(A)):
            leftSum += A[i] - A[i - L] 
            lookLeft[i] = max(lookLeft[i - 1], leftSum)
        lookRight = [float('-inf')] * len(A)
        rightSum = sum(A[-M:])
        lookRight[len(A) - M] = rightSum
        for j in xrange(len(A) - M - 1, -1, -1):
            rightSum += A[j] - A[j + M]
            lookRight[j] = max(lookRight[j + 1], rightSum)
        max_result = max(lookLeft[k] + lookRight[k + 1] for k in xrange(L - 1, len(A) - M))
        if mayNeedSwap and L != M:
            max_result = max(max_result, self.maxSumTwoNoOverlap(A, M, L, False))
        return max_result
        
