MOD = 10 ** 9 + 7
class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit2shift = {1 << shift : shift for shift in xrange(0, 31)}
        def getMask(num):
            for shift in (1, 2, 4, 8, 16):
                num |= num >> shift
            return num
            
        res = 0
        for i in xrange(1, n + 1):
            mask = getMask(i)
            shift = bit2shift[mask + 1]
            res <<= shift
            res |= i
            res %= MOD
        # print(res)
        # print(int(res, 2))
        return res

