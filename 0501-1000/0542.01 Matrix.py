class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        delta = (1, 0, -1, 0, 1)
        def neighbors(i, j):
            for k in xrange(4):
                x, y = i + delta[k], j + delta[k + 1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and res[x][y] is None:
                    yield x, y
        queue = collections.deque([(i, j, 0) for i in xrange(len(matrix)) for j in xrange(len(matrix[0])) if matrix[i][j] == 0])
        res = [[None] * len(matrix[0]) for _ in matrix]
        for i, j, _ in queue:
            res[i][j] = 0
        while queue:
            i, j, dist = queue.popleft()
            for nx, ny in neighbors(i, j):
                res[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
        return res
