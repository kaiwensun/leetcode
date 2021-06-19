class Solution(object):
    def largestArea(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        grid = map(list, grid)
        M, N = len(grid), len(grid[0])
        DELTA = (1, 0, -1, 0, 1)

        def valid(i, j):
            return 0 <= i < M and 0 <= j < N

        def valid_neighbors(i, j):
            for k in xrange(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if valid(x, y):
                    yield x, y

        def dfs_adjacent0(i, j):
            is_valid = valid(i, j)
            theme = grid[i][j] if is_valid else "0"

            if is_valid:
                grid[i][j] = ""

            for x, y in valid_neighbors(i, j):
                if grid[x][y] and (theme == "0" or grid[x][y] == theme):
                    dfs_adjacent0(x, y)

        def dfs_area_size(i, j):
            res = 1
            theme, grid[i][j] = grid[i][j], ""
            for x, y in valid_neighbors(i, j):
                if grid[x][y] == theme:
                    res += dfs_area_size(x, y)
            return res

        for i in xrange(-1, M + 1):
            for j in xrange(-1, N + 1):
                if not valid(i, j) or grid[i][j] == "0":
                    dfs_adjacent0(i, j)
        res = 0
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]:
                    res = max(res, dfs_area_size(i, j))
        return res

