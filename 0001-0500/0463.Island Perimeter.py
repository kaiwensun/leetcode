class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DELTA = (1, 0, -1, 0, 1)
        def isIsland(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and bool(grid[i][j])
        def dfs(i, j):
            if isIsland(i, j):
                if grid[i][j] == 2:
                    return 0
                grid[i][j] = 2
                res = 0
                for k in xrange(4):
                    res += dfs(i + DELTA[k], j + DELTA[k + 1])
                return res
            else:
                return 1
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
