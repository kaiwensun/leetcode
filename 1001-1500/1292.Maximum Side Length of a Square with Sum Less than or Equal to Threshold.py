class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        
        def initAcc():
            for i in xrange(1, m + 1):
                for j in xrange(1, n + 1):
                    acc[i][j] = acc[i - 1][j] + acc[i][j - 1] - acc[i - 1][j - 1] + mat[i - 1][j - 1]
                
        def squareSum(i, j, edge):
            return acc[i + edge][j + edge] - acc[i][j + edge] - acc[i + edge][j] + acc[i][j]
        
        def squareExists(edge):
            for i in xrange(m - edge + 1):
                for j in xrange(n - edge + 1):
                    if squareSum(i, j, edge) <= threshold:
                        return True
            return False
        m, n = len(mat), len(mat[0])
        acc = [[0] * (n + 1) for _ in xrange(m + 1)]
        initAcc()
        start, end = 1, min(m, n) + 1
        while start < end:
            mid = (start + end) / 2
            if squareExists(mid):
                start = mid + 1
            else:
                end = mid
        return end - 1
