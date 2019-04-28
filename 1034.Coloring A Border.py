class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        old = grid[r0][c0]
        def dfs(r, c):
            if not(0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return True
            if grid[r][c] in (-1, -2):
                return False
            if grid[r][c] != old:
                return True
            grid[r][c] = -2
            delta = (1, 0, -1, 0, 1)
            for i in xrange(4):
                dx, dy = delta[i], delta[i + 1]
                if dfs(r + dx, c + dy):
                    grid[r][c] = -1
            return False
        dfs(r0, c0)
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = color
                elif grid[i][j] == -2:
                    grid[i][j] = old
                    
        return grid
