class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        for row in grid:
            area += max(row)
            area += len(list(filter(bool, row)))
        for j in xrange(len(grid[0])):
            area += max(grid[i][j] for i in xrange(len(grid)))
        return area
