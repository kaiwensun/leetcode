class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def find1():
            for i in xrange(len(A)):
                for j in xrange(len(A[0])):
                    if A[i][j] == 1:
                        return i, j
        def neighbors(i, j):
            DELTA = (1, 0, -1, 0, 1)
            for index in xrange(4):
                x, y = i + DELTA[index], j + DELTA[index + 1]
                if 0 <= x < len(A) and 0 <= y < len(A[0]):
                    yield x, y
        def fillQueue(i, j):
            if A[i][j] == 1:
                A[i][j] = 2
                queue.append((i, j))
                for ni, nj in neighbors(i, j):
                    fillQueue(ni, nj)
        def bfs():
            res = 0
            while queue:
                i, j = queue.popleft()
                if i == "#":
                    res += 1
                    queue.append(("#", "#"))
                    continue
                for ni, nj in neighbors(i, j):
                    if A[ni][nj] == 1:
                        queue.clear()
                        break
                    if A[ni][nj] == 0:
                        queue.append((ni, nj))
                        A[ni][nj] = -1
            return res
                    
        startX, startY = find1()
        queue = collections.deque()
        fillQueue(startX, startY)
        queue.append(("#", "#"))
        return bfs()
