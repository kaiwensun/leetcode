MOD = 10 ** 9 + 7

class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [
            [1, 0, 0], # absent 0 days. late 0, 1, 2 times
            [0, 0, 0] # absent 1 day. late 0, 1, 2 times
        ]
        """
        dp = [
            [a0l0, a0l1, a0l2],
            [a1l0, a1l1, a1l2]
        ]
        next_dp = [
            [a0l*, a0l0, a0l1],
            [a*l*, a1l0, a1l1]
        ]
        """
        for _ in range(n + 1):
            dp = [
                [sum(dp[0]) % MOD, dp[0][0], dp[0][1]],
                [(sum(dp[0]) + sum(dp[1])) % MOD, dp[1][0], dp[1][1]]
            ]
        return dp[1][0]

