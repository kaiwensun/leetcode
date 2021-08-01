MOD = 10 ** 9 + 7

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        res = 0
        # number of partial-special subsequens ended with [0, 1, 2]
        dp = [0, 0, 0]
        for num in nums:
            if num == 0:
                dp[0] += dp[0] + 1
            elif num == 1:
                dp[1] += dp[0] + dp[1]
            else:  # num == 2
                dp[2] += dp[1] + dp[2]
            dp[num] %= MOD
        return dp[2]

