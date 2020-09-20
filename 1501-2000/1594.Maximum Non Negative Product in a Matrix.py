from functools import lru_cache
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(i, j):
            num = grid[i][j]
            if i == j == 0:
                return num, num
            mn, mx = float("inf"), float("-inf")
            if i != 0:
                up_mn, up_mx = dp(i - 1, j)
                mn = min(mn, up_mn * num, up_mx * num)
                mx = max(mx, up_mn * num, up_mx * num)
            if j != 0:
                left_mn, left_mx = dp(i, j - 1)
                mn = min(mn, left_mn * num, left_mx * num)
                mx = max(mx, left_mn * num, left_mx * num)
            return mn, mx
        MOD = 10 ** 9 + 7
        res = dp(len(grid) - 1, len(grid[0]) - 1)[1]
        return -1 if res < 0 else res % MOD

