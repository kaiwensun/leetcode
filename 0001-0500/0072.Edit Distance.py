"""
Basic idea:
    Dynamic programming
Result:
    1146 / 1146 test cases passed.
    Status: Accepted
    Runtime: 284 ms
    Your runtime beats 77.67% of python submissions.
Date:
    6/26/2016
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*(len(word2)+1) for i in xrange(len(word1)+1)]
        for i in xrange(len(word1)+1):
            dp[i][0]=i
        for j in xrange(len(word2)+1):
            dp[0][j]=j
        for i in xrange(1,len(word1)+1):
            for j in xrange(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[len(word1)][len(word2)]
        
