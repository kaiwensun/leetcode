class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        cntx = [0] * len(mat)
        cnty = [0] * len(mat[0])
        for i in xrange(len(mat)):
            for j in xrange(len(mat[i])):
                cntx[i] += mat[i][j]
                cnty[j] += mat[i][j]
        res = 0
        for i in xrange(len(mat)):
            for j in xrange(len(mat[i])):
                if cntx[i] == cnty[j] == mat[i][j] == 1:
                    res += 1
        return res

