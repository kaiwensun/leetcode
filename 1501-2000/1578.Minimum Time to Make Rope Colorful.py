class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        # DP is not the optimal splution.
        letter_set = set(s)
        letter_set.add("^")
        dp = {c: 0 if c == s[0] else cost[0] for c in letter_set}
        for i in xrange(1, len(s)):
            dp[s[i]] = min(dp[s[i]] + cost[i], min(dp[c] for c in letter_set if c != s[i]))
            for c in letter_set:
                if c != s[i]:
                    dp[c] += cost[i]
        return min(dp.values())

