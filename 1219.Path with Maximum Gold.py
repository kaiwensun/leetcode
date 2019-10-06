import functools
class Solution:
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        delta = (1, 0, -1, 0, 1)
        def canVisit(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]
        @functools.lru_cache(None)
        def walk(visitedSet, i, j):
            gold = grid[i][j]
            grid[i][j] = 0
            visitedSet = visitedSet.union({(i, j)})
            res = 0
            for k in range(4):
                di, dj = delta[k], delta[k + 1]
                if canVisit(i + di, j + dj):
                    res = max(res, walk(visitedSet, i + di, j + dj))
            grid[i][j] = gold
            return res + gold
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if canVisit(i, j):
                    res = max(res, walk(frozenset(), i, j))
        return res
