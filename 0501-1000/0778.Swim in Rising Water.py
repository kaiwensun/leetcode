class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        DELTA = (-1, 0, 1, 0, -1)
        data = {(i, j) : (i, j) for i in xrange(N) for j in xrange(N)}

        def find(x):
            if x != data[x]:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry

        def expand(i, j):
            for k in xrange(4):
                ni, nj = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] <= grid[i][j]:
                    union((i, j), (ni, nj))

        cells = sorted((grid[i][j], i, j) for i in xrange(N) for j in xrange(N))
        for level, i, j in cells:
            expand(i, j)
            if find((0, 0)) == find((N - 1, N - 1)):
                return level
        assert(False)

