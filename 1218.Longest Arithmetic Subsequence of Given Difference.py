import collections
class Solution(object):
    def longestSubsequence(self, arr, diff):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        for a in arr:
            dp[a] = max(dp[a], dp[a - diff] + 1)
        return max(dp.values())
