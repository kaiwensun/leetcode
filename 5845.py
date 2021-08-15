class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cells = [(i - 1, j - 1) for (i, j) in cells]
        flooded = set(map(tuple, cells))
        data = {(i, j):(i, j) for i in range(row) for j in range(col)}
        top, bottom = (-1, -1), (-2, -2)
        data[top] = top
        data[bottom] = bottom
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
        
        for i in range(row - 1):
            for j in range(col - 1):
                if (i, j) in flooded:
                    continue
                for (ni, nj) in ((i + 1, j), (i, j + 1)):
                    if (ni, nj) in flooded:
                        continue
                    union((i, j), (ni, nj))
        
        for j in range(col):
            if (0, j) not in flooded:
                union((0, j), top)
            if (row - 1, j) not in flooded:
                union((row - 1, j), top)
        
        for t in range(len(cells) - 1, -1, -1):
            i, j = cells[t]
            if i == 0:
                union(top, (i, j))
            if i == row - 1:
                union(bottom, (i, j))
            flooded.remove((i, j))
            for k in range(4):
                ni, nj = i + DELTA[k], j + DELTA[k + 1]
                if not (0 <= ni < row and 0 <= nj < col):
                    continue
                if (ni, nj) in flooded:
                    continue
                union((ni, nj), (i, j))
            if find(top) == find(bottom):
                break
        return t

