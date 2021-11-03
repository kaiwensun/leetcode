import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        def neighbors(i, j):
            for k in range(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < M and 0 <= y < N:
                    yield x, y

        DELTA = (1, 0, -1, 0, 1)
        M, N = len(heightMap), len(heightMap[0])
        queue = [(0, i, j) for i in range(M) for j in (-1, N)] + [(0, i, j) for i in (-1, M) for j in range(N)]
        res = 0
        while queue:
            h, i, j = heapq.heappop(queue)
            for x, y in neighbors(i, j):
                if heightMap[x][y] < 0:
                    continue
                if heightMap[x][y] <= h:
                    res += h - heightMap[x][y]
                    heapq.heappush(queue, (h, x, y))
                else:
                    heapq.heappush(queue, (heightMap[x][y], x, y))
                heightMap[x][y] = -1
        return res

