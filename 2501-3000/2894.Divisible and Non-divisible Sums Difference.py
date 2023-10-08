class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num2 = (1 + n // m) * (n // m) // 2 * m
        num1 = (1 + n) * n // 2 - num2
        return num1 - num2

