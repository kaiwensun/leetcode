from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        scnt = Counter(s)
        tcnt = Counter(t)
        res = 0
        for c in set(s) | set(t):
            res += abs(scnt[c] - tcnt[c])
        return res / 2
