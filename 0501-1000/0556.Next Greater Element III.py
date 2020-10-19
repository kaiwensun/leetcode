import bisect
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        for i in xrange(len(s) - 1, 0, -1):
            if s[i] > s[i - 1]:
                tail = "".join(sorted(s[i - 1:]))
                for j in xrange(1, len(tail)):
                    if tail[j] > s[i - 1]:
                        res = int(s[:i - 1] + tail[j] + tail[:j] + tail[j + 1:])
                        return res if res <= 1 << 31 - 1 else -1
        return -1

