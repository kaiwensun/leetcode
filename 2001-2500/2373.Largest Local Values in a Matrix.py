class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        res = [[None] * (N - 2) for _ in range(M - 2)]
        for i in range(M - 2):
            for j in range(N - 2):
                res[i][j] = max(max(grid[k][j: j + 3]) for k in range(i, i + 3))
        return res

