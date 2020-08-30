class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        DELTA = [1, 0, -1, 0, 1]
        def getNeighbors(i, j):
            for k in range(4):
                x = i + DELTA[k]
                y = j + DELTA[k + 1]
                if isLand(x, y):
                    yield x, y

        def isLand(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 0

        def fill(i, j, value):
            if grid[i][j] == 0 or grid[i][j] == value:
                return 0
            grid[i][j] = value
            res = 1
            for x, y in getNeighbors(i, j):
                res += fill(x, y, value)
            return res
        
        def findALand():
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] != 0:
                        return i, j
        
        def check(i, j):
            nonlocal check_value
            check_value += 1
            res = float('inf')
            if grid[i][j] != 0:
                old_val = grid[i][j]
                grid[i][j] = 0
                for x, y in getNeighbors(i, j):
                    if isLand(x, y):
                        if lands - 1 != fill(x, y, check_value):
                            # disconnected
                            res = min(res, 1)
                        break
                grid[i][j] = old_val
                cnt_neighbors = len(tuple(getNeighbors(i, j)))
                if cnt_neighbors == 1 and lands == 2:
                    res = 2
                else:
                    res = min(res, cnt_neighbors)
            return res

        check_value = 2
        lands = sum(map(sum, grid))
        if lands == 0:
            # no land exists
            return 0
        x, y = findALand()
        dfs_lands = fill(x, y, check_value)
        if lands != dfs_lands:
            # already disconnected
            return 0

        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = min(res, check(i, j))
                if res == 1:
                    # fast succeed
                    break
        return res
