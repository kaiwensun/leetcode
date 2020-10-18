class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        def calc_relative_reachables(radius):
            res = []
            r2 = radius ** 2
            for i in xrange(-radius, radius + 1):
                i2 = i**2
                for j in xrange(-radius, radius + 1):
                    if i2 + j ** 2 <= r2:
                        res.append((i, j, math.sqrt(i ** 2 + j ** 2)))
            return res
        W = max(tower[0] for tower in towers)
        H = max(tower[1] for tower in towers)
        relative_reachables = calc_relative_reachables(radius)
        grid = [[0] * (H + 1) for _ in xrange(W + 1)]
        for x, y, q in towers:
            for i, j, d in relative_reachables:
                if 0 <= x + i <= W and 0 <= y + j <= H:
                    grid[x + i][y + j] += q // (1 + d)
        sig = 0
        res = None
        for x in xrange(W + 1):
            for y in xrange(H + 1):
                if grid[x][y] > sig:
                    sig = grid[x][y]
                    res = [x, y]
        return res

