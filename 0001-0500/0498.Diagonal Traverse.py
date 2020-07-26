class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        delta_r, delta_c = -1, 1
        rval = [None] * (len(matrix) * len(matrix[0]))
        row = col = 0
        for i in xrange(len(rval)):
            rval[i] = matrix[row][col]
            row += delta_r
            col += delta_c
            if row == len(matrix):
                row -= 1
                col += 2
                delta_r, delta_c = -delta_r, -delta_c
            elif col == len(matrix[0]):
                row += 2
                col -= 1
                delta_r, delta_c = -delta_r, -delta_c
            elif row == -1:
                row = 0
                delta_r, delta_c = -delta_r, -delta_c
            elif col == -1:
                col = 0
                delta_r, delta_c = -delta_r, -delta_c
        return rval
