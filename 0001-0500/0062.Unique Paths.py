class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.uniquePaths(n, m)
        dp = [1] * m
        for _ in xrange(n - 1):
            for j in xrange(1, m):
                dp[j] += dp[j - 1]
        return dp[-1]
