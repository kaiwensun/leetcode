class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        DELTA = [1, 0, -1, 0, 1]
        m, n = len(grid), len(grid[0])
        def get_total_value(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] <= 0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            for t in range(4):
                dx, dy = DELTA[t], DELTA[t + 1]
                res += get_total_value(i + dx, j + dy)
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                val = get_total_value(i, j)
                if val and val % k == 0:
                    res += 1
        return res

