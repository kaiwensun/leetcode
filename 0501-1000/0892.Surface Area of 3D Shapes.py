class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                left = 0 if j == 0 else grid[i][j - 1]
                up = 0 if i == 0 else grid[i - 1][j]
                height = grid[i][j]
                area += max(height - left, 0) + max(height - up, 0) + (1 if height else 0)
        return area * 2
