"""
Result:
  229 / 229 test cases passed.
  Status: Accepted
  Runtime: 100 ms
  Your runtime beats 22.26% of pythonsubmissions.
Idea:
    Dynamic programming. 
    - subtask: dp[i] means the length of longest valid paraentheses ending at s[i]
    - bigger task expressed in smaller task: dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2] if s[i-dp[i-1]-1] is '(' and s[i] is ')' (be careful about array boundary); 0 otherwise
    ......[....]([.....])...
                        i
    - basecase: dp[0]=0
Date:
  5/27/2016
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]*len(s)
        m = 0   #max length
        for i in xrange(1,len(s)):
            left = i-dp[i-1]-1
            if left>=0 and s[left]=='(' and s[i]==')':
                dp[i]=dp[i-1]+2
                if left-1>=0:
                    dp[i]+=dp[left-1]
                m = max(m,dp[i])
        return m
