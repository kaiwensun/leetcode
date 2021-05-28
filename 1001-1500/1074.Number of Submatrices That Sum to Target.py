"""
Hint: instead of a 2D matrix, how would you solve a similar problem on 1D array?
"""

from collections import Counter

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        M, N = len(matrix), len(matrix[0])

        for i in xrange(1, M):
            for j in xrange(N):
                matrix[i][j] += matrix[i - 1][j]
        matrix.append([0] * N)

        def strip_sum(i1, i2):
            for j in xrange(N):
                yield matrix[i2][j] - matrix[i1 - 1][j]
        res = 0
        for i1 in xrange(M):
            for i2 in xrange(i1, M):
                sm = 0
                cnt = Counter({0: 1})
                for num in strip_sum(i1, i2):
                    sm += num
                    res += cnt[sm - target]
                    cnt[sm] += 1
        return res

