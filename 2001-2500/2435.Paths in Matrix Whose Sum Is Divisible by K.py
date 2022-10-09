from collections import Counter
from functools import cache

MOD = 10 ** 9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i, j):
            if i == m or j == n:
                return Counter()
            if i == m - 1 and j == n - 1:
                return Counter({grid[-1][-1] % k: 1})
            sm = dp(i + 1, j) + dp(i, j + 1)
            cell = grid[i][j]
            return Counter({(key + cell) % k: val % MOD for key, val in sm.items()})
        return dp(0, 0)[0]

