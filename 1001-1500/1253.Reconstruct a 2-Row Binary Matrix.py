from collections import Counter
class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        cnt = Counter(colsum)
        upper -= cnt[2]
        lower -= cnt[2]
        if upper < 0 or lower < 0 or upper + lower != cnt[1]:
            return []
        res = [[0] * len(colsum) for _ in xrange(2)]
        print cnt
        for i in xrange(len(colsum)):
            if colsum[i] == 1:
                res[upper == 0][i] = 1
                if upper:
                    upper -= 1
            elif colsum[i] == 2:
                res[0][i] = res[1][i] = 1
        return res
