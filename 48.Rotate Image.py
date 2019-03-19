class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix) - 1
        for i in xrange((len(matrix) + 1) // 2):
            for j in xrange(len(matrix) // 2):
                matrix[i][j], matrix[N - j][i], matrix[N - i][N - j], matrix[j][N - i] = matrix[N - j][i], matrix[N - i][N - j], matrix[j][N - i], matrix[i][j]
