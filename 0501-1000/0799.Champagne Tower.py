class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        row = [poured]
        for i in xrange(1, query_row + 1):
            next_row = [0] * (len(row) + 1)
            excess = 0
            for j in xrange(len(next_row)):
                if j == 0 or j == len(next_row) - 1:
                    next_row[j] = max(0, row[0] - 1) / 2.0
                else:
                    next_row[j] = (max(0, row[j - 1] - 1) + max(0, row[j] - 1)) / 2.0
                excess = max(excess, next_row[j])
            if excess == 0:
                return 0.0
            row = next_row
        return min(1.0, row[query_glass])

