class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        dp = [1] * len(A[0])
        for j in xrange(len(A[0])):
            for k in xrange(j):
                if dp[j] < dp[k] + 1:
                    for i in xrange(len(A)):
                        if A[i][k] > A[i][j]:
                            break
                    else:
                        dp[j] = dp[k] + 1
        return len(A[0]) - max(dp)
