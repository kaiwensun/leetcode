from collections import defaultdict

class EnrichedColor:
    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.left = self.n
        self.right = 0
        self.top = self.m
        self.bottom = 0
        self.actual_exposed = set()
        self.full_area = None
        
    def colorSeenAt(self, i, j):
        self.left = min(self.left, j)
        self.right = max(self.right, j)
        self.top = min(self.top, i)
        self.bottom = max(self.bottom, i)
        self.full_area = (self.bottom - self.top + 1) * (self.right - self.left + 1)
        self.actual_exposed.add((i, j))
        
    def isCovering(self, i, j):
        return self.top <= i <= self.bottom and self.left <= j <= self.right
    
    def isFullyExposed(self):
        return self.full_area == len(self.actual_exposed)
        
    def pointsCovered(self):
        for i in xrange(self.top, self.bottom + 1):
            for j in xrange(self.left, self.right + 1):
                yield i, j

    def exposePoint(self, i, j):
        if self.isCovering(i, j):
            self.actual_exposed.add((i, j))
    
    def jointPointsWith(self, other):
        for i in xrange(max(self.top, other.top), min(self.bottom, other.bottom) + 1):
            for j in xrange(max(self.left, other.left), min(self.right, other.right) + 1):
                yield i, j
                
    def __str__(self):
        return "Enriched([l, r, t, b] is [%s, %s, %s, %s]. filled by %s)" % (self.left, self.right, self.top, self.bottom, len(self.actual_exposed))
            
class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        m, n = len(targetGrid), len(targetGrid[0])
        colorManager = defaultdict(lambda: EnrichedColor(targetGrid))
        for i in xrange(m):
            for j in xrange(n):
                color = targetGrid[i][j]
                colorManager[color].colorSeenAt(i, j)
        exposed_colors = set(color for color, enriched in colorManager.iteritems() if enriched.isFullyExposed())
        unexposed_colors = set(colorManager.keys()) - exposed_colors
        
        while exposed_colors:
            color = exposed_colors.pop()
            enriched = colorManager[color]
            # print "I pick", color, "to free. Its current status is", enriched
            for other_color in tuple(unexposed_colors):
                for i, j in enriched.jointPointsWith(colorManager[other_color]):
                    colorManager[other_color].exposePoint(i, j)
                    # print("I expose other color %s at point (%s, %s)" % (other_color, i, j))
                    if colorManager[other_color].isFullyExposed() and other_color in unexposed_colors:
                        unexposed_colors.remove(other_color)
                        exposed_colors.add(other_color)
        return len(unexposed_colors) == 0

