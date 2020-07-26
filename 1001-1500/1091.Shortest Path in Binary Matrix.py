class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getLength(i, j):
            return grid[i][j] >> 1
        def setLength(i, j, v):
            # safely assume grid[i][j] >> 1 is 0
            grid[i][j] |= v << 1
        def getGrid(i, j):
            return grid[i][j] & 1
        def getAdj(i, j):
            return [(r, c) for r in xrange(i - 1, i + 2)
                for c in xrange(j - 1, j + 2)
                    if (
                        not (i == c and j == r) and
                        0 <= r < len(grid) and
                        0 <= c < len(grid[0]) and
                        getGrid(r, c) == 0 and
                        getLength(r, c) == 0)]
        
        if grid[0][0] or grid[-1][-1]:
            return -1
        setLength(0, 0, 1)
        queue = collections.deque([(0, 0)])
        while queue:
            cell = queue.popleft()
            length = getLength(*cell)
            adjs = getAdj(*cell)
            for adj in adjs:
                setLength(*adj, v=length + 1)
                queue.append(adj)
        return getLength(-1, -1) if getLength(-1, -1) else -1
