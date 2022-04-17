class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def calc_factor(num):
            res = 0
            while not num % 2:
                res += 1
                num //= 2
            while not num % 5:
                res += 1j
                num //= 5
            return res

        M, N = len(grid), len(grid[0])
        factor_grid = [
            [calc_factor(num) for num in row]
            for row in grid
        ]

        prefixes = [
            [
                [0 for _1 in range(N)] for _2 in range(M)
            ] for _3 in range(4)
        ]
        for i in range(M):
            acc0 = acc1 = 0
            for j in range(N):
                prefixes[0][i][j] = acc0
                prefixes[1][i][N - 1 - j] = acc1
                acc0 += factor_grid[i][j]
                acc1 += factor_grid[i][N - 1 - j]

        for j in range(N):
            acc2 = acc3 = 0
            for i in range(M):
                prefixes[2][i][j] = acc2
                prefixes[3][M - 1 - i][j] = acc3
                acc2 += factor_grid[i][j]
                acc3 += factor_grid[M - 1 - i][j]

        def get_grid_cell(i, j, g):
            return g[i][j] if 0 <= i < M and 0 <= j < N else 0

        def get_cell_max(i, j):
            center = get_grid_cell(i, j, factor_grid)
            branches = [get_grid_cell(i, j, table) for table in prefixes]
            res = 0
            for x in range(len(branches)):
                for y in range(x + 1, len(branches)):
                    total = branches[x] + branches[y] + center
                    score = int(min(total.real, total.imag))
                    res = max(res, score)
            return res

        return max(get_cell_max(i, j) for i in range(M) for j in range(N))

