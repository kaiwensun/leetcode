import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        rval = []
        while n:
            n -= 1
            digit = n % 26
            c = string.ascii_uppercase[digit]
            rval.append(c)
            n /= 26
        rval.reverse()
        return ''.join(rval)
