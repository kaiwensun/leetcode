class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        DELTA = (0, 0, 1, 1, 0)
        @lru_cache(None)
        def dp(i, i_back, dist):
            j = dist - i
            j_back = dist - i_back
            if max(i, i_back) >= M or max(j, j_back) >= M:
                return float("-inf")
            if grid[i][j] == -1 or grid[i_back][j_back] == -1:
                return float("-inf")
            if dist == M + N - 2:
                return grid[-1][-1]
            res = float("-inf")
            for k in range(4):
                di, di_back = DELTA[k], DELTA[k + 1]
                res = max(res, dp(i + di, i_back + di_back, dist + 1))
            if i == i_back:
                return res + grid[i][j]
            else:
                return res + grid[i][j] + grid[i_back][j_back]
        return max(0, dp(0, 0, 0))

