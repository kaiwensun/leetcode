import heapq

class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = 0
        queue = []
        for i in xrange(len(matrix)):
            left = 0
            for j in xrange(len(matrix[i])):
                left ^= matrix[i][j]
                if i == 0:
                    matrix[i][j] = left
                else:
                    matrix[i][j] = left ^ matrix[i - 1][j]
                if len(queue) < k:
                    heapq.heappush(queue, matrix[i][j])
                else:
                    heapq.heappushpop(queue, matrix[i][j])
        return queue[0]


