class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        while k:
            n -= 1
            cur = min(26, k - n)
            res.append(chr(ord("a") + cur - 1))
            k -= cur
        return "".join(reversed(res))

