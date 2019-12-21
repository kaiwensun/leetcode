class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        delta = (1, 0, -1, 0, 1)
        m, n = len(grid), len(grid[0])
        def neighbors(x, y):
            for i in xrange(4):
                dx, dy = delta[i], delta[i + 1]
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    yield (x + dx, y + dy)
        distance = [[[None] * (k + 1) for _ in xrange(n)] for __ in xrange(m)]
        
        def dfs(i, j, remainK):
            if remainK < 0:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return 0
            if remainK >= m - i + n - j - 2:
                # 【Optimization】
                return m - i + n - j - 2
            if distance[i][j][remainK] is None:
                res = distance[i][j][remainK] = float('inf')
                for neighbor in neighbors(i, j):
                    x, y = neighbor[0], neighbor[1]
                    res = min(res, dfs(x, y, remainK - grid[x][y]))
                distance[i][j][remainK] = res + 1
            return distance[i][j][remainK]
        res = dfs(0, 0, k - grid[0][0])
        return res if res != float('inf') else -1
