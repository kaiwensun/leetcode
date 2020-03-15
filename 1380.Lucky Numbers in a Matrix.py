class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = map(min, matrix)
        col = map(max, zip(*matrix))
        res = []
        print col
        print row
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == row[i] == col[j]:
                    res.append(matrix[i][j])
        return res
