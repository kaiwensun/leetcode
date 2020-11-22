from bisect import bisect_right
class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        n_str = str(n)
        length = len(n_str)
        res = sum(len(digits) ** l for l in xrange(1, length + 1))
        digits.sort()
        for i in xrange(length):
            posi = bisect_right(digits, n_str[i])
            res -= (len(digits) - posi) * len(digits) ** (length - i - 1)
            if posi == 0 or n_str[i] != digits[posi - 1]:
                break
        return res

