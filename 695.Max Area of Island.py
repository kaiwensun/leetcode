class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        delta = (1, 0, -1, 0, 1)
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = -1
            s = 1
            for k in xrange(4):
                dx, dy = delta[k], delta[k + 1]
                s += dfs(i + dx, j + dy)
            return s
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                res = max(res, dfs(i, j))
        return res
