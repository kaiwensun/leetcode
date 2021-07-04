class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        return (pow(5, (n + 1) // 2, MOD) * pow(4, n // 2, MOD)) % MOD

