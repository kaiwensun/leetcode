class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        res = sum(mat[i][i] + mat[i][n - 1 - i] for i in xrange(n))
        return res - mat[n // 2][n // 2] if n % 2 else res

