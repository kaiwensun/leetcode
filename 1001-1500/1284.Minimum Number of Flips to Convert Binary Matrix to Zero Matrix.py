import collections
class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        dp = {}
        mat = tuple(map(tuple, mat))
        def getNeighbors(i, j):
            res = [(i, j)]
            if i != 0:
                res.append((i - 1, j))
            if i != m - 1:
                res.append((i + 1, j))
            if j != 0:
                res.append((i, j - 1))
            if j != n - 1:
                res.append((i, j + 1))
            return res
        def flip(mat, i, j):
            mat = list(map(list, mat))
            for x, y in getNeighbors(i, j):
                mat[x][y] = 1 - mat[x][y]
            mat = tuple(map(tuple, mat))
            return mat
        def isAllZeros(mat):
            for row in mat:
                if sum(row) != 0:
                    return False
            return True
        # bfs
        if isAllZeros(mat):
            return 0
        queue = collections.deque()
        seen = set()
        seen.add(mat)
        queue.append((mat, 0))
        while queue:
            source, step = queue.popleft()
            for i in xrange(m):
                for j in xrange(n):
                    target = flip(source, i, j)
                    if target in seen:
                        continue
                    if isAllZeros(target):
                        return step + 1
                    seen.add(target)
                    queue.append((target, step + 1))
        return -1
        
