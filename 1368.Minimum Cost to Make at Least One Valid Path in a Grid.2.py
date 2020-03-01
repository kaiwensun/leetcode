import collections
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def genNeighbors(point):
            for dxy in sign2dxy.values():
                if 0 <= point[0] + dxy[0] < m and 0 <= point[1] + dxy[1] < n:
                    yield (point[0] + dxy[0], point[1] + dxy[1])

        def discover(point, queue):
            if not (0 <= point[0] < m and 0 <= point[1] < n):
                return False
            if point == (m - 1, n - 1):
                return True
            sign = grid[point[0]][point[1]]
            if sign == VISITED_SIGN:
                return False
            grid[point[0]][point[1]] = VISITED_SIGN
            dxy = sign2dxy[sign]
            if discover((point[0] + dxy[0], point[1] + dxy[1]), queue):
                return True
            for neighbor in genNeighbors(point):
                if grid[neighbor[0]][neighbor[1]] != VISITED_SIGN:
                    queue.append(neighbor)
            return False
            
        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return 0
        outsiders = {(m - 1, n - 1)}
        sign2dxy = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        VISITED_SIGN = -1
        queue = collections.deque([(0, 0), "#"])
        cost = 0
        while len(queue) > 1:
            point = queue.popleft()
            if point == "#":
                queue.append(point)
                cost += 1
                continue
            if discover(point, queue):
                return cost
        return cost
