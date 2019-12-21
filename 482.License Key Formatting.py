class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = "".join(S.split("-")).upper()
        return "-".join(reversed(tuple(s[-i - K:-i or None] for i in xrange(0, len(s), K))))
