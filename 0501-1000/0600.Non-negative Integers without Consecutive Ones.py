from functools import cache

class Solution:
    def findIntegers(self, n: int) -> int:
        bits = bin(n)[2:]

        @cache
        def dp(i, was_one, is_smaller_than_n):
            if i == len(bits):
                return 1
            bit = bits[i]
            # current bit set to 0
            res = dp(i + 1, False, is_smaller_than_n or bit == '1')
            if not was_one and (is_smaller_than_n or bit == '1'):
                res += dp(i + 1, True, is_smaller_than_n)
            return res
        return dp(0, False, False)

