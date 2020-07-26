import functools
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @functools.lru_cache(None)
        def dp(steps, posi):
            if steps == 0:
                return 1 if posi == 0 else 0
            res = dp(steps - 1, posi)
            if posi > 0:
                res += dp(steps - 1, posi - 1)
                res %= MOD
            if posi < arrLen - 1:
                res += dp(steps - 1, posi + 1)
                res %= MOD
            return res
        MOD = 10**9 + 7
        return dp(steps, 0)
