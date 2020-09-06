class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        total, mx = 0, float("-inf")
        res = 0
        for i, c in enumerate(s):
            total += cost[i]
            mx = max(mx, cost[i])
            if i == len(s) - 1 or s[i] != s[i + 1]:
                res += total - mx
                total, mx = 0, float("-inf")
        return res

