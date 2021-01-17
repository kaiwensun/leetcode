class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in xrange(1, len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]
        for row in matrix:
            row.sort(reverse=True)
            for j in xrange(len(row)):
                res = max(res, (j + 1) * row[j])
        return res

