from functools import cache

MOD = 10 ** 9 + 7

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        str_len = max(len(num1), len(num2))
        num1 = '0' * (str_len - len(num1)) + num1
        num2 = '0' * (str_len - len(num2)) + num2

        @cache
        def dp(i: int, num1_is_0: bool, num2_is_9: bool, cur_sum: int) -> int:
            if cur_sum > max_sum:
                return 0
            if i == str_len:
                return 1 if min_sum <= cur_sum else 0
            d1 = 0 if num1_is_0 else int(num1[i])
            d2 = 9 if num2_is_9 else int(num2[i])
            res = 0
            for d in range(d1, d2 + 1):
                res += dp(i + 1, num1_is_0 or d != d1, num2_is_9 or d != d2, cur_sum + d)
            res %= MOD
            return res

        return dp(0, False, False, 0)

