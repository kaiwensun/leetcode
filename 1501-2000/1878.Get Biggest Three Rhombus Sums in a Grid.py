from functools import lru_cache
from bisect import insort

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dp(i, j, size, direction):
            if size == 1:
                return grid[i][j]
            else:
                return grid[i][j] + dp(i - 1 * direction, j + 1, size - 1, direction)

        def rhombus_sum(i, j, size):
            if size == 0:
                return grid[i][j]
            else:
                assert not(i - size < 0 or i + size >= M or j + size * 2 >= N)
                return dp(i, j, size, 1) + dp(i - size, j + size, size, -1) + dp(i + size - 1, j + size + 1, size, 1) + dp(i + 1, j + 1, size, -1)
        
        def add_result(sm):
            if -sm not in res:
                insort(res, -sm)
            if len(res) > 3:
                res.pop()

        
        res = []
        for i in range(M):
            for j in range(N):
                for size in range(min(i + 1, M - i, (N + 1 - j) // 2)):
                    add_result(rhombus_sum(i, j, size))
        return [-sm for sm in res]

