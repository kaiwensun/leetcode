class Solution(object):
    dp = [1]
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= len(Solution.dp) - 1:
            return Solution.dp[n]
        res = sum(self.numTrees(i) * self.numTrees(n - 1 - i) for i in xrange(n / 2))
        res *= 2
        if n % 2:
            res += self.numTrees(n / 2) * self.numTrees(n / 2)
        Solution.dp.append(res)
        return res
