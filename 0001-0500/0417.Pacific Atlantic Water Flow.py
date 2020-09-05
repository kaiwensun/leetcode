class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return []
        height = len(matrix)
        width = len(matrix[0])
        
        both_collector = set()
        self.climb(matrix, height - 1, 0, matrix[height - 1][0] - 1, both_collector)
        self.climb(matrix, 0, width - 1, matrix[0][width - 1] - 1, both_collector)
        pacific_collector = both_collector.copy()
        atlantic_collector = both_collector.copy()
        for col in xrange(width):
            self.climb(matrix, 0, col, matrix[0][col] - 1, pacific_collector)
            self.climb(matrix, height - 1, col, matrix[height - 1][col] - 1, atlantic_collector)
        for row in xrange(height):
            self.climb(matrix, row, 0, matrix[row][0] - 1, pacific_collector)
            self.climb(matrix, row, width - 1, matrix[row][width - 1] - 1, atlantic_collector)
        return list(atlantic_collector.intersection(pacific_collector))
        
    
    def climb(self, matrix, row, col, prev_elev, collector):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return
        if prev_elev > matrix[row][col]:
            return
        if (row, col) in collector:
            return
        collector.add((row, col))
        for r, c in zip((row - 1, row, row + 1, row), (col, col + 1, col, col - 1)):
                self.climb(matrix, r, c, matrix[row][col], collector)

