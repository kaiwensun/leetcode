class Solution:
    def isThree(self, n: int) -> bool:
        res = 1
        for i in range(1, n):
            if n % i == 0:
                res += 1
            if res > 3:
                break
        return res == 3

