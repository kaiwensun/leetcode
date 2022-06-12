from functools import cache

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        @cache
        def dp(i, j):
            if i == M - 1:
                return grid[i][j]
            res = float("inf")
            for next_j in range(N):
                res = min(res, dp(i + 1, next_j) + moveCost[grid[i][j]][next_j])
            return grid[i][j] + res

        return min(dp(0, j) for j in range(N))

