class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.roten = []
        self.fresh = 0
        self.getRoten(grid)
        if self.fresh == 0:
            return 0
        if len(self.roten) == 0:
            return -1
        # self.roten.insert(0, '#')
        self.roten.append('#')
        minute = self.becomeRoten(grid)
        if self.fresh != 0:
            return -1
        return minute
        
        
        
    
    def getRoten(self, grid):
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    self.fresh += 1
                if grid[i][j] == 2:
                    self.roten.append((i, j))
    
    def becomeRoten(self, grid):
        minute = 0
        effective = False
        while self.roten:
            rot, roten = self.roten[0], self.roten[1:]
            self.roten = roten
            if rot == '#':
                if effective:
                    minute += 1
                    self.roten.append('#')
                    effective = False
                else:
                    break 
            else:
                i, j = rot
                effective = self.rotenSingle(i + 1, j, grid) or effective
                effective = self.rotenSingle(i - 1, j, grid) or effective
                effective = self.rotenSingle(i, j + 1, grid) or effective
                effective = self.rotenSingle(i, j - 1, grid) or effective
        return minute
    
    def rotenSingle(self, i, j, grid):
        effective = False
        if i >= 0 and i < len(grid):
            if j >= 0 and j < len(grid[0]):
                if grid[i][j] == 1:
                    self.fresh -= 1
                    grid[i][j] = 2
                    self.roten.append((i, j))
                    effective = True
        return effective
        
