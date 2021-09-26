class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
            grid[1][n - i - 1] += grid[1][n - i]
        res = float("inf")
        for i in range(n):
            res = min(res, max(grid[1][0] - grid[1][i], grid[0][-1] - grid[0][i]))
        return res

