class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        def test(num):
            s = str(num)
            if len(s) % 2:
                return False
            l = len(s) // 2
            return sum(map(int, s[-l:])) == sum(map(int, s[:l]))
        res = 0
        for n in range(low, high + 1):
            if test(n):
                res += 1
        return res

