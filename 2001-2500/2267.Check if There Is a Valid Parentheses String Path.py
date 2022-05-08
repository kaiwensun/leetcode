from functools import cache

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        M, N = len(grid), len(grid[0])
        if (M + N) % 2 == 0:
            return False
        @cache
        def dp(i, j, opened):
            if not (0 <= i < M and 0 <= j < N):
                return False
            if opened == 0 and grid[i][j] == ')':
                return False
            if i + j + opened > M + N - 1:
                return False
            if i == M - 1 and j == N - 1:
                return opened == 1 and grid[i][j] == ')'
            diff = 1 if grid[i][j] == '(' else -1
            return dp(i + 1, j, opened + diff) or dp(i, j + 1, opened + diff)
        return dp(0, 0, 0)

