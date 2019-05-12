class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0] * len(A)
        for i in xrange(len(A)):
            mygroup = 0
            for ahead in xrange(min(K, i + 1)):
                mygroup = max(mygroup, A[i - ahead])
                dp[i] = max(dp[i], (0 if i == ahead else dp[i - ahead - 1]) + mygroup * (ahead + 1))
        return dp[-1]
