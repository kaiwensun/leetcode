class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        res = []
        for i in xrange(max(map(len, words))):
            row = "".join(word[i:i+1] or ' ' for word in words)
            res.append(row.rstrip())
        return res
