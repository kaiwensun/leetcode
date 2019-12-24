import functools
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        delta = (1, 0, -1, 0, 1)
        MOD = 10 ** 9 + 7
        
        @functools.lru_cache(None)
        def dp(i, j, move):
            if 0 <= i < m and 0 <= j < n:
                if move == 0:
                    return 0
                else:
                    return sum(dp(i + delta[_], j + delta[_ + 1], move - 1) for _ in range(4)) % MOD
            else:
                return 1
        return dp(i, j, N)
