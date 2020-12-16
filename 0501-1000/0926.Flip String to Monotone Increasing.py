class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        S = map(int, S)
        S.append(0)
        total_ones = sum(S)
        ones = 0
        res = float("inf")
        for i in xrange(len(S)):
            res = min(res, ones + len(S) - i - (total_ones - ones) - 1)
            ones += S[i]
        return res

