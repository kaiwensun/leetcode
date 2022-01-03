class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        res = 1
        for i in range(left, right + 1):
            res *= i
        zeros = 0
        while res % 10 == 0:
            res //= 10
            zeros += 1
        s = str(res)
        if len(s) > 10:
            return f"{s[:5]}...{s[-5:]}e{zeros}"
        else:
            return f"{s}e{zeros}"

