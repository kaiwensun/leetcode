from collections import Counter
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        cntr = Counter(s)
        cntl = Counter()
        res = 0
        for i in xrange(len(s) - 1):
            c = s[i]
            cntl[c] += 1
            cntr[c] -= 1
            res = max(res, cntl["0"] + cntr["1"])
        return res
