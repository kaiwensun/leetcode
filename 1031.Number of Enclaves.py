class Solution(object):
    delta = (0, 1, 0, -1, 0)
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(A)):
            self.dfs(A, i, 0)
            self.dfs(A, i, len(A[0]) - 1)
        for j in xrange(len(A[0])):
            self.dfs(A, 0, j)
            self.dfs(A, len(A) - 1, j)
        return sum([sum(row) for row in A])
        
    def dfs(self, A, i, j):
        if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]) or A[i][j] == 0:
            return
        A[i][j] = 0
        for index in xrange(4):
            di, dj = self.delta[index: index + 2]
            self.dfs(A, i + di, j + dj)
