from functools import lru_cache

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        M, N = len(grid), len(grid[0])
        @lru_cache(None)
        def prefix(i, j, di, dj):
            return grid[i][j] + prefix(i + di, j + dj, di, dj) if 0 <= i < M and 0 <= j < N else 0

        def row_prefix(i, j):
            return prefix(i, j, 0, -1)
            
        def row_sum(i, j, size):
            return row_prefix(i, j + size - 1) - row_prefix(i, j - 1)

        def col_prefix(i, j):
            return prefix(i, j, -1, 0)

        def col_sum(i, j, size):
            return col_prefix(i + size - 1, j) - col_prefix(i - 1, j)

        def diag_prefix(i, j):
            return prefix(i, j, -1, -1)
            
        def diag_sum(i, j, size):
            return diag_prefix(i + size - 1, j + size - 1) - diag_prefix(i - 1, j - 1)

        def anti_diag_prefix(i, j):
            return prefix(i, j, -1, 1)

        def anti_diag_sum(i, j, size):
            return anti_diag_prefix(i, j) - anti_diag_prefix(i - size, j + size)

        def test(i, j, size):
            target = diag_sum(i, j, size)
            if target != anti_diag_sum(i + size - 1, j, size):
                return False
            for x in range(i, i + size):
                if row_sum(x, j, size) != target: return False
            for y in range(j, j + size):
                if col_sum(i, y, size) != target: return False
            return True

        def test_size(size):
            for i in range(M - size + 1):
                for j in range(N - size + 1):
                    if test(i, j, size):
                        return True
            return False
        
        for size in range(min(M, N), 0, -1):
            if test_size(size): return size
        return 0

