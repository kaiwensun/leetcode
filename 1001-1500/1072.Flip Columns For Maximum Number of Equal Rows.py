class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter()
        for row in matrix:
            if row[0]:
                counter[tuple(row)] += 1
            else:
                counter[tuple(1 - i for i in row)] += 1
        return counter.most_common(1)[0][1]
