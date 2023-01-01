class Solution:
    def countDigits(self, num: int) -> int:
        return sum(num % int(c) == 0 for c in str(num))

