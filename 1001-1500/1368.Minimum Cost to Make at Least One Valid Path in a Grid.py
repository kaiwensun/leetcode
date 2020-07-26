class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        outsiders = {(m - 1, n - 1)}
        grid[-1][-1] = -2
        DELTA = (-1, 0, 1, 0, -1)
        sign2dxy = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        VISITED_SIGN = -1
        
        def is_pointing_to_me(sign, dxy):
            return sign2dxy[sign] == dxy
        
        def expandLayer(point, outsiders):
            if grid[point[0]][point[1]] == VISITED_SIGN:
                return
            grid[point[0]][point[1]] = VISITED_SIGN
            for i in xrange(4):
                dx, dy = DELTA[i], DELTA[i + 1]
                new_point = (point[0] + dx, point[1] + dy)
                
                if not (0 <= new_point[0] < m and 0 <= new_point[1] < n):
                    continue
                sign = grid[new_point[0]][new_point[1]]
                if sign == VISITED_SIGN:
                    # visited or outsiders
                    continue
                if is_pointing_to_me(sign, (-dx, -dy)):
                    expandLayer(new_point, outsiders)
                else:
                    outsiders.add(new_point)

        cost = 0
        while grid[0][0] != -1:
            snapshot_outsiders = list(outsiders)
            outsiders = set()
            for point in snapshot_outsiders:
                expandLayer(point, outsiders)
                grid[point[0]][point[1]] = VISITED_SIGN
            cost += 1
        return cost - 1
