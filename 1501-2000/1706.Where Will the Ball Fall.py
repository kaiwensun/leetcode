class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        M, N = len(grid), len(grid[0])
        def dfs(i, j):
            if i == M:
                return j
            if grid[i][j] == 1 and j != N - 1 and grid[i][j + 1] == 1:
                return dfs(i + 1, j + 1)
            if grid[i][j] == -1 and j != 0 and grid[i][j - 1] == -1:
                return dfs(i + 1, j - 1)
            return -1
        return [dfs(0, j) for j in xrange(N)]

