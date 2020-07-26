class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        M, N = len(text1), len(text2)
        dp = [0] * N
        for m in xrange(M):
            upleft = 0
            for n in xrange(N):
                if text1[m] == text2[n]:
                    cell = max(
                        n and dp[n - 1],
                        m and dp[n],
                        (m and n and upleft) + 1
                    )
                else:
                    cell = max(n and dp[n - 1], m and dp[n])
                upleft, dp[n] = dp[n], cell
        return dp[-1]
