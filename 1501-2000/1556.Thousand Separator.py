class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n:
            cur = n % 1000
            n //= 1000
            fmt = "%03d" if n else "%d"
            res.append(str(fmt % cur))
        if not res:
            res.append("0")
        return ".".join(reversed(res))
