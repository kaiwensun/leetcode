from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        DELTA = [1, 0, -1, 0, 1]
        m, n = len(grid), len(grid[0])
        def neighbors(i, j):
            for k in range(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        def fill(i, j, value):
            grid[i][j] = value
            for x, y in neighbors(i, j):
                if grid[x][y] == 0:
                    fill(x, y, value)
                elif grid[x][y] == 1:
                    grid[x][y] = value - 1
                    queue.append((x, y))

        queue = deque()
        fill(0, 0, -1)
        while not grid[-1][-1]:
            i, j = queue.popleft()
            for x, y in neighbors(i, j):
                if grid[x][y] == 1:
                    grid[x][y] = grid[i][j] - 1
                    queue.append((x, y))
                elif grid[x][y] == 0:
                    fill(x, y, grid[i][j])
        return ~grid[-1][-1]

