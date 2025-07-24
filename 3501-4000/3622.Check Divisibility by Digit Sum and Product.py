import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = sum(map(int, str(n)))
        p = math.prod(map(int, str(n)))
        d = s + p
        return n % d == 0
