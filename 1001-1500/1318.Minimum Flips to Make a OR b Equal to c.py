class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def getBit(num, i):
            return (num & (1 << i)) >> i
        res = 0
        for i in xrange(32):
            if getBit(c, i):
                res += 1 - ((getBit(a, i) | getBit(b, i)))
            else:
                res += getBit(a, i) + getBit(b, i)
        return res
