class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        # init grid
        grid = [[N for i in xrange(N)] for j in xrange(N)]   #each cel of 2D table is [up, down, left, right]
        for mine in mines:
            grid[mine[0]][mine[1]] = -1
        deltas = (1, 0, -1, 0, 1)
        starts = ((0, 0), (N - 1, N - 1), (N - 1, N - 1), (0, 0))
        for i in xrange(4):
            dx, dy = deltas[i : i + 2]
            startx, starty = starts[i]
            for j in xrange(N):
                currx, curry = startx, starty
                strike = 0
                for k in xrange(N):
                    if grid[currx][curry] == -1: 
                        strike = 0
                    else:
                        strike += 1
                        grid[currx][curry] = min(grid[currx][curry], strike)
                    currx += dx
                    curry += dy
                startx += dy
                starty += dx
        rval = 0
        for row in grid:
            rval = max(rval, max(row))
        return rval

