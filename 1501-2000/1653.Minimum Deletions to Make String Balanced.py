class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnts = [0] * len(s)
        bcnt = 0
        for i, c in enumerate(s):
            cnts[i] = bcnt
            bcnt += int(c == "b")
        acnt = 0
        for i, c in reversed(tuple(enumerate(s))):
            cnts[i] += acnt
            acnt += int(c == "a")
        return min(cnts)

