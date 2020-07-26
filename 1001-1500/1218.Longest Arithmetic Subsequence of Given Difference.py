# Learning from this question:
# Use `collections.Counter()`, instead of `collections.defaultdict(int)`.

import collections
class Solution(object):
    def longestSubsequence(self, arr, diff):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = collections.Counter()
        for a in arr:
            dp[a] = max(dp[a], dp[a - diff] + 1)
        return max(dp.values())
