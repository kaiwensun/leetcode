class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        k %= m * n
        line = sum(grid, [])
        line = line[-k:] + line[:-k]
        return [line[i * n: (i + 1) * n]for i in range(m)]
