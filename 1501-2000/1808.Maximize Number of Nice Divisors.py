class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        MOD = 10 ** 9 + 7
        if primeFactors % 3 == 1:
            return (pow(3, primeFactors // 3 - 1, MOD) * 4) % MOD
        elif primeFactors % 3 == 2:
            return (pow(3, primeFactors // 3, MOD) * 2) % MOD
        else:
            return pow(3, primeFactors // 3, MOD)

