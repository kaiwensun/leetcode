class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [{} for _ in xrange(len(A))]
        res = 1
        for i in xrange(len(A)):
            dp[i].setdefault(0, 1)
            for j in xrange(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[j][diff] = max(dp[j].get(diff, 2), dp[i].get(diff, 0) + 1)
                res = max(res, dp[j][diff])
        return res
