from functools import cache

class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        @cache
        def dp(i, num, residual, diff, is_limit, is_leading):
            if len(num) - i < abs(diff):
                return 0
            if i == len(num):
                return 1 if residual == 0 else 0
            res = 0
            mx = int(num[i]) if is_limit else 9
            for d in range(0, mx + 1):
                diff_delta = 1 if d % 2 else -1
                if d == 0 and is_leading:
                    diff_delta = 0
                res += dp(i + 1, num, (residual * 10 + d) % k, diff + diff_delta, is_limit and d == mx, is_leading and d == 0)
            return res
        return dp(0, str(high), 0, 0, True, True) - dp(0, str(low - 1), 0, 0, True, True)

