from math import factorial

class Solution(object):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        p_cnt = bisect.bisect_right(self.primes, n)
        return (factorial(p_cnt) % (10**9 + 7)) * (factorial(n - p_cnt) % (10**9 + 7)) % (10**9 + 7)
