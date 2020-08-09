from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        DELTA = (1, 0, -1, 0, 1)
        def adjacents(i, j):
            for k in xrange(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    yield (x, y)
                    
        queue = deque()
        fresh = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        queue.append("#")
        day = 0
        while len(queue) > 1:
            cell = queue.popleft()
            if cell == "#":
                queue.append(cell)
                day += 1
                continue
            for x, y in adjacents(*cell):
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    queue.append((x, y))
        return -1 if fresh else day

