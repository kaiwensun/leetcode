import functools
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i == j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')
            return min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]
        return dp(len(grid) - 1, len(grid[0]) - 1)
