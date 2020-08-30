class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        DELTA = [-1, 0, 1, 0, -1]
        def neighbors(i, j):
            for k in xrange(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    yield x, y

        def dfs(i, j, c, from_i, from_j):
            if grid[i][j] == ord(c):
                return True
            if grid[i][j] != c:
                return False
            grid[i][j] = ord(c)
            for x, y in neighbors(i, j):
                if not(x == from_i and y == from_j) and dfs(x, y, c, i, j):
                    return True
            return False

        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if isinstance(grid[i][j], unicode):
                    if dfs(i, j, grid[i][j], None, None):
                        return True
        return False
