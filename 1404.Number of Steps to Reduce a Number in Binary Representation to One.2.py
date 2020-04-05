class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        owe = 0
        cnt1 = 0
        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == "0":
                res += 1 + owe
            else:
                cnt1 += 1
                res += 1
                owe = 1
        return res + owe - (2 if cnt1 == 1 else 0)
