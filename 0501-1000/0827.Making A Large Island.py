DELTA = (1, 0, -1, 0, 1)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        data = {(i, j): (i, j) for i in range(n) for j in range(n) if grid[i][j]}
        size = {(i, j): 1 for i in range(n) for j in range(n) if grid[i][j]}

        def get_neighbors(point):
            i, j = point
            neighbors = []
            for k in range(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if not (0 <= x < n and 0 <= y < n):
                    continue
                if not grid[x][y]:
                    continue
                neighbors.append((x, y))
            return neighbors

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry
                size[ry] += size[rx]

        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    continue
                for k in range(4):
                    x, y = i + DELTA[k], j + DELTA[k + 1]
                    if not (0 <= x < n and 0 <= y < n):
                        continue
                    if not grid[x][y]:
                        continue
                    union((i, j), (x, y))

        res = max(size.values()) if size else 0
        if len(size) < n * n:
            res += 1
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    continue
                neighbor_islands = {find(neighbor) for neighbor in get_neighbors((i, j))}
                if not neighbor_islands:
                    continue
                sum_size = sum(size[neighbor_island] for neighbor_island in neighbor_islands) + 1
                res = max(res, sum_size)
        return res

