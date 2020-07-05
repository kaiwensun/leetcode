class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        def span(i, j):
            res = 0
            min_width = float("inf")
            for row_index in xrange(i, -1, -1):
                min_width = min(min_width, mat[row_index][j])
                if min_width == 0:
                    break
                res += min_width
            print i, j, res
            return res
    
        res = 0
        for i in xrange(len(mat)):
            for j in xrange(len(mat[i])):
                if j != 0 and mat[i][j] == 1:
                    mat[i][j] += mat[i][j - 1]
                res += span(i, j)
        print mat
        return res
