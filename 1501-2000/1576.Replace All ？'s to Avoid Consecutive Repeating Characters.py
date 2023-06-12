class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in xrange(len(s)):
            if s[i] != '?':
                continue
            for c in "abc":
                if s[i - 1] == c or s[(i + 1) % len(s)] == c:
                    continue
                break
            s[i] = c
        return "".join(s)

