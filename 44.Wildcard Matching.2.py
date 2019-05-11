class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        dp[i][j] is a (bool, bool) tuple.
        The first of the tuple means:
        - Do s[:i] and p[:j] match?
        The second of the tuple means:
        - Is there a (true, bool) among dp[x][j] where x <= i ?
        """
        dp = [None] * (len(p) + 1)
        dp[0] = (True, True)
        for i in xrange(1, len(p) + 1):
            dp[i] = (dp[i - 1][0] and p[i - 1] == '*',) * 2
        for c in s:
            topleft = dp[0]
            dp[0] = (False, True)
            for j in xrange(1, len(p) + 1):
                if p[j - 1] == '?':
                    res = topleft[0], topleft[0] or dp[j][1]
                elif p[j - 1] == '*':
                    res = dp[j - 1][1] or dp[j][1]
                    res = res, res
                else:
                    res = topleft[0] and p[j - 1] == c
                    res = res, res or dp[j][1]
                topleft, dp[j] = dp[j], res
        return dp[-1][0]
