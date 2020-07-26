class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        left = [[None] * n for _ in xrange(m)]
        right = [[None] * n for _ in xrange(m)]
        up = [[None] * n for _ in xrange(m)]
        down = [[None] * n for _ in xrange(m)]
        for i in xrange(m):
            left[i][0] = grid[i][0]
            right[i][-1] = grid[i][-1]
            for j in xrange(1, n):
                left[i][j] = 0 if grid[i][j] == 0 else left[i][j - 1] + 1
                right[i][-1 - j] = 0 if grid[i][-1 - j] == 0 else right[i][-j] + 1
        for j in xrange(n):
            up[0][j] = grid[0][j]
            down[-1][j] = grid[-1][j]
            for i in xrange(1, m):
                up[i][j] = 0 if grid[i][j] == 0 else up[i - 1][j] + 1
                down[-1 - i][j] = 0 if grid[-1 - i][j] == 0 else down[-i][j] + 1
        res = 0
        for i1 in xrange(m):
            for j1 in xrange(n):
                mn1 = min(right[i1][j1], down[i1][j1])
                for edge in xrange(0, mn1 + 1):
                    i2 = i1 + edge - 1
                    j2 = j1 + edge - 1
                    if i2 < m and j2 < n and up[i2][j2] >= edge and left[i2][j2] >= edge:
                        res = max(res, edge)
        return res * res
