class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        DELTA = (1, 0, -1, 0, 1)
        M, N = len(grid1), len(grid1[0])

        def valid(i, j):
            return 0 <= i < M and 0 <= j < N

        def neighbors(i, j):
            for k in range(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if valid(x, y):
                    yield x, y

        def dfs(i, j, marker):
            if grid2[i][j] == 0 or grid2[i][j] == marker:
                return True
            if grid2[i][j] != 1:
                return False
            grid2[i][j] = marker
            if grid1[i][j] == 0:
                return False
            for x, y in neighbors(i, j):
                if not dfs(x, y, marker):
                    return False
            return True

        res = 0
        marker = 2
        for i in range(M):
            for j in range(N):
                if grid2[i][j] == 1:
                    marker += 1
                    res += dfs(i, j, marker)
        return res

