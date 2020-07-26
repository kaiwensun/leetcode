class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(A)):
            if A[i][0] == 0:
                A[i] = [1 - ele for ele in A[i]]
        result = 0
        for j in xrange(len(A[0])):
            ones = 0
            for row in A:
                ones += row[j]
            major = max(ones, len(A) - ones)
            result += major * (1 << (len(A[0]) - 1 - j))
        return result
