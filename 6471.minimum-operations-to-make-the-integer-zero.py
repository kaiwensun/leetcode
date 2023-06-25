class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        cur = num1
        res = 0
        stop = num1
        while True:
            stop -= 1 + num2
            if num2 > 0 and stop < 0:
                return -1
            res += 1
            cur -= num2
            if res <= cur and bin(cur).count('1') <= res:
                return res

