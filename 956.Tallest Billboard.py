class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        MAX_DIFF = (sum(rods) + 1) / 2 + 1
        # dp[i][d] means using the first i rods to construct two supporters having difference d, what is the maximum total length of the two supporters?
        dp = [[float('-inf')] * MAX_DIFF for _ in xrange(len(rods) + 1)]
        dp[0][0] = 0
        for i in xrange(1, len(rods) + 1):
            new_rod = rods[i - 1]
            for new_diff in xrange(MAX_DIFF):
                for old_diff in [abs(new_diff - new_rod), new_diff + new_rod]:
                    if old_diff >= MAX_DIFF:
                        continue
                    dp[i][new_diff] = max(dp[i][new_diff], dp[i - 1][new_diff], dp[i - 1][old_diff] + new_rod)
        return max(dp[len(rods)][0] / 2, 0)
