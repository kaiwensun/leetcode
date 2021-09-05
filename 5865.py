MOD = 10 ** 9 + 7
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [[0, 1] for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + 1) % MOD
            dp[i][1] = (dp[i][0] + 1 + dp[i][0] - dp[nextVisit[i]][0]) % MOD
        return dp[-1][0]

