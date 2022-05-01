from collections import deque

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        DELTA = [1, 0, -1, 0, 1]
        M, N = len(grid), len(grid[0])

        def neighbors(i, j):
            for k in range(4):
                di, dj = DELTA[k], DELTA[k + 1]
                x, y = i + di, j + dj
                if 0 <= x < M and 0 <= y < N:
                    yield x, y
            
        fires = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    grid[i][j] = float("inf")
                elif grid[i][j] == 1:
                    fires.append([i, j])
                elif grid[i][j] == 2:
                    grid[i][j] = float("-inf")

        fires.append(None)
        fire_step = 2
        while len(fires) > 1:
            node = fires.popleft()
            if node:
                for x, y in neighbors(*node):
                    if grid[x][y] == float("inf"):
                        grid[x][y] = fire_step
                        fires.append([x, y])
            else:
                fire_step += 1
                fires.append(node)

        walk_time = [[None] * N for _ in range(M)]
        walk_time[0][0] = 1
        walk_step = 2
        walk = deque([[0, 0], None])
        while len(walk) > 1:
            node = walk.popleft()
            if node:
                for x, y in neighbors(*node):
                    if walk_time[x][y] is None and (grid[x][y] - walk_step > 0 or (x == M - 1 and y == N - 1)):
                        walk_time[x][y] = walk_step
                        walk.append([x, y])
            else:
                if walk_time[-1][-1] is not None:
                    break
                walk_step += 1
                walk.append(node)
        if walk_time[-1][-1] is None:
            return -1
        if grid[-1][-1] == float("inf"):
            return 10 ** 9
        for x, y in neighbors(M - 1, N - 1):
            if grid[x][y] > grid[-1][-1] and walk_time[x][y]:
                return grid[-1][-1] - walk_time[-1][-1]
        return grid[-1][-1] - walk_time[-1][-1] - 1

