class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        a, b = len(A), len(B)
        dp = [[0] * b for _ in xrange(a)]
        dp[0][0] = int(A[0] == B[0])
        for i in xrange(1, a):
            dp[i][0] = dp[i - 1][0] or int(A[i] == B[0])
        for j in xrange(1, b):
            dp[0][j] = dp[0][j - 1] or int(A[0] == B[j])
        for i in xrange(1, a):
            for j in xrange(1, b):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if A[i] == B[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]
