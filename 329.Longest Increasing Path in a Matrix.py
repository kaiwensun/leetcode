import functools
class Solution:
    deltas = (1, 0, -1, 0, 1)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        optimal = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                optimal = max(optimal, self.dfs(i, j))
        return optimal

    @functools.lru_cache(None)
    def dfs(self, i, j):
        rval = 1
        for p in range(4):
            dx, dy = self.deltas[p], self.deltas[p + 1]
            if self.get_height(i + dx, j + dy) > self.matrix[i][j]:
                rval = max(self.dfs(i + dx, j + dy) + 1, rval)
        return rval
        
        
    def get_height(self, i, j):
        if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0]):
            return self.matrix[i][j]
        else:
            return float('-inf')
