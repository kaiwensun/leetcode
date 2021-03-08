class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        res = [[None] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if isWater[i][j]:
                    res[i][j] = 0
        queue = collections.deque((i, j) for i in xrange(m) for j in xrange(n) if isWater[i][j])

        def get_empty_neighbors(i, j):
            DELTA = (1, 0, -1, 0, 1)
            for k in xrange(4):
                x, y = i + DELTA[k], j + DELTA[k + 1]
                if 0 <= x < m and 0 <= y < n and res[x][y] is None:
                    yield x, y
        height = 1
        queue.append((None, None))
        while len(queue) > 1:
            i, j = queue.popleft()
            if i is None:
                height += 1
                queue.append((None, None))
                continue
            for x, y in get_empty_neighbors(i, j):
                res[x][y] = height
                queue.append((x, y))
        return res

