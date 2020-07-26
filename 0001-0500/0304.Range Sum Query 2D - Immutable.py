class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self._m = matrix
        for i in xrange(len(matrix)):
            left_sum = 0
            for j in xrange(len(matrix[0])):
                left_sum += matrix[i][j]
                top = 0 if i == 0 else matrix[i - 1][j]
                matrix[i][j] = left_sum + top
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        matrix = self._m
        total = matrix[row2][col2]
        left = 0 if col1 == 0 else matrix[row2][col1 - 1]
        top = 0 if row1 == 0 else matrix[row1 - 1][col2]
        topleft = 0 if row1 == 0 or col1 == 0 else matrix[row1 - 1][col1 - 1]
        return total - top - left + topleft
