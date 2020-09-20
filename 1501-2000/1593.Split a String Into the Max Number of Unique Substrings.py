class Solution(object):
    def maxUniqueSplit(self, s, used=set()):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        for split in xrange(1, len(s) + 1):
            cur = s[:split]
            if cur not in used:
                used.add(cur)
                res = max(res, self.maxUniqueSplit(s[split:], used) + 1)
                used.remove(cur)
        return res

