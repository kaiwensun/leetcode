class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        res = [[0] * len(colSum) for _ in xrange(len(rowSum))]
        for i in xrange(len(rowSum)):
            for j in xrange(len(colSum)):
                mn = min(rowSum[i], colSum[j])
                rowSum[i] -= mn
                colSum[j] -= mn
                res[i][j] = mn
        return res

