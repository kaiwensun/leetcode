import functools
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i, j1, j2):
            if not (i < len(grid) and 0 <= j1 < len(grid[0]) and 0 <= j2 < len(grid[0])):
                return 0
            if j1 == j2:
                pick = grid[i][j1]
            else:
                pick = grid[i][j1] + grid[i][j2]
            res = 0
            for d1 in (-1, 0, 1):
                for d2 in (-1, 0, 1):
                    res = max(res, dp(i + 1, j1 + d1, j2 + d2))
            return pick + res
        return dp(0, 0, len(grid[0]) - 1)
