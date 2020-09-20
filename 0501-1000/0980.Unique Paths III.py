class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        scanResult = self.scan(grid)
        start, end, empty_cnt = scanResult['start'], scanResult['end'], scanResult['empty']
        result = self.walk(grid, start[0], start[1], empty_cnt)
        return result
        
        
    def scan(self, grid):
        result = {'empty': 0}
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    result['start'] = (i, j)
                elif cell == 2:
                    result['end'] = (i, j)
                elif cell == 0:
                    result.setdefault('empty', 0)
                    result['empty'] += 1
                else:
                    result.setdefault('block', 0)
                    result['block'] += 1
        return result

    def walk(self, grid, i, j, steps):
        result = 0
        for target in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if target[0] < 0 or target[0] >= len(grid) or target[1] < 0 or target[1] >= len(grid[0]):
                continue
            cell = grid[target[0]][target[1]]
            if cell == 1:
                continue
            elif cell == 2:
                if steps == 0:
                    result = 1
                    break
                continue
            elif cell == 0:
                grid[target[0]][target[1]] = 3
                rec = self.walk(grid, target[0], target[1], steps - 1)
                result += rec
                grid[target[0]][target[1]] = 0
                continue
            else:
                continue
        return result

