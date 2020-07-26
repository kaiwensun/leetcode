class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        delta = (1, 0, -1, 0, 1)
        def neighbors(x, y):
            for i in xrange(4):
                dx, dy = delta[i], delta[i + 1]
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                    yield x + dx, y + dy
        def dfs(i, j):
            if grid[i][j] != "1":
                return False
            grid[i][j] = "2"
            for nx, ny in neighbors(i, j):
                dfs(nx, ny)
            return True
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                res += dfs(i, j)
        return res
