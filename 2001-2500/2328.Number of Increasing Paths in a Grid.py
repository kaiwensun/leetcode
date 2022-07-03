from functools import cache

MOD = 10 ** 9 + 7
DELTA = [1, 0, -1, 0, 1]

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def neighbors(i, j):
            for k in range(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        @cache
        def dp(i, j):
            res = 1
            for x, y in neighbors(i, j):
                if grid[x][y] >= grid[i][j]:
                    continue
                res += dp(x, y)
            return res % MOD

        return sum(dp(i, j) for i in range(m) for j in range(n)) % MOD

