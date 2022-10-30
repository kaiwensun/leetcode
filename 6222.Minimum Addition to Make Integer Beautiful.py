class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(num):
            return sum(map(int, str(num)))
        def digit_arr(num):
            return list(reversed(list(map(int, '0' + str(num)))))
        if digit_sum(n) <= target:
            return 0
        if digit_sum(n + 1) <= target:
            return 1
        narr = digit_arr(n)
        x = 0
        for i in range(len(narr)):
            x += (10 - narr[i]) * 10 ** i
            if digit_sum(n + x) <= target:
                return x
            narr = digit_arr(n + x)
        return x

