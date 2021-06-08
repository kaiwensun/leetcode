from functools import lru_cache

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        N = len(group)
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, remain_profit, remain_member):
            if remain_member < 0:
                return 0
            if i == N:
                return int(remain_profit <= 0)
            return (dp(i + 1, remain_profit, remain_member) + dp(i + 1, max(0, remain_profit - profit[i]), max(-1, remain_member - group[i]))) % MOD

        return dp(0, minProfit, n)

