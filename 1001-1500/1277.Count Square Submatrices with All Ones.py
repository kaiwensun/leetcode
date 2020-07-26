import functools
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0 or j == 0:
                return matrix[i][j]
            if matrix[i][j] == 0:
                return 0
            left = dp(i, j - 1)
            up = dp(i - 1, j)
            upleft = dp(i - 1, j - 1)
            return min(left, up, upleft) + 1
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += dp(i, j)
        return res
