class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sumOdd = (1 + 2 * n - 1) * n // 2 = n * n
        # sumEven = (0 + 2 * n) * (n + 1) // 2 = n * (n + 1)
        # gcd(sumOdd, sumEven) = gcd(n * n, n * (n + 1)) = n
        return n

