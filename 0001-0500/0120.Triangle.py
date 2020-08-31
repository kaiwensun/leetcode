class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i - 1][k] for k in [j - 1, j] if 0 <= k < len(triangle[i - 1]))
        return min(triangle[-1])

