class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        noop = {(i, j) for i, j in hits if grid[i][j] == 0}
        for i, j in hits:
            grid[i][j] = 0
        M, N = len(grid), len(grid[0])

        data = {(i, j):(i, j) for i in xrange(-1, M) for j in xrange(N) if grid[i][j] or i == -1}
        area_size = Counter({(i, j):0 if i == -1 else 1 for (i, j) in data.keys()})
        dummy_top = (-1, 0)
        data[dummy_top] = dummy_top
        area_size[dummy_top] = 0
        DELTA = (1, 0, -1, 0, 1)
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry
                area_size[ry] += area_size[rx]
                del area_size[rx]
                return True
            return False

        def get(i, j):
            return (i == -1 or grid[i][j]) if -1 <= i < M and 0 <= j < N else None

        def dfs_connect(i, j):
            if not get(i, j):
                return
            for k in xrange(4):
                new_i, new_j = i + DELTA[k], j + DELTA[k + 1]
                if get(new_i, new_j) and union((i, j), (new_i, new_j)):
                    dfs_connect(new_i, new_j)

        dfs_connect(*dummy_top)

        for i in xrange(M):
            for j in xrange(N):
                dfs_connect(i, j)
        res = []
        for x, y in reversed(hits):
            if get(x, y) or (x, y) in noop:
                res.append(0)
                continue
            old_connected = area_size[find(dummy_top)]
            grid[x][y] = 1
            data[(x, y)] = (x, y)
            area_size[(x, y)] = 1
            for k in xrange(4):
                new_x, new_y = x + DELTA[k], y + DELTA[k + 1]
                if get(new_x, new_y):
                    union((x, y), (new_x, new_y))
            new_connected = area_size[find(dummy_top)]
            res.append(max(0, new_connected - old_connected - 1))
        return list(reversed(res))

