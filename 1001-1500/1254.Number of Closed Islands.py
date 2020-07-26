class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        DELTA = (1, 0, -1, 0, 1)
        # return -1: is at edge of grid
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return -1
            if grid[i][j] != 0:
                return 0
            grid[i][j] = 2 # visited
            res = 1
            for k in range(4):
                dx, dy = DELTA[k], DELTA[k + 1]
                rec = dfs(i + dx, j + dy)
                if rec == -1 or res == -1:
                    res = -1
                else:
                    res += rec
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += 0 < dfs(i, j)
        return res
