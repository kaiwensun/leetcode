class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        def genIndex(diagonal):
            if diagonal < m:
                x, y = m - diagonal - 1, 0
            else:
                x, y = 0, diagonal - m + 1
            while x < m and y < n:
                yield x, y
                x += 1
                y += 1

        for diagonal in xrange(m + n - 1):
            arr = sorted(mat[x][y] for x, y in genIndex(diagonal))
            for i, (x, y) in enumerate(genIndex(diagonal)):
                mat[x][y] = arr[i]
        return mat
