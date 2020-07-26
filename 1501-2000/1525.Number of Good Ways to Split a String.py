from collections import Counter
class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        lcnt, rcnt = Counter(), Counter(s)
        res = 0
        for c in s:
            lcnt[c] += 1
            rcnt[c] -= 1
            if rcnt[c] == 0:
                del rcnt[c]
            if len(lcnt) == len(rcnt):
                res += 1
        return res
