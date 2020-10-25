import heapq

DELTA = (1, 0, -1, 0, 1)

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        
        def neighbors(i, j):
            for k in xrange(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                    yield x, y
                    
        DELTA = (1, 0, -1, 0, 1)
        visited = [[False] * len(heights[0]) for _ in xrange(len(heights))]
        # (effort from top-left, i, j)
        queue = [(0, 0, 0)]
        
        while queue:
            effort, i, j = heapq.heappop(queue)
            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                return effort
            if visited[i][j]:
                continue
            visited[i][j] = True
            for x, y in neighbors(i, j):
                heapq.heappush(queue, (max(effort, abs(heights[i][j] - heights[x][y])), x, y))
        assert(False)

