from functools import cache
from itertools import product

MOD = 10 ** 9 + 7
class Solution:
    def countPalindromes(self, s: str) -> int:
        @cache
        def dp(i, string, direction):
            if not 0 <= i < len(s):
                return 0
            if len(string) == 1:
                return int(s[i] == string) + dp(i + direction, string, direction)
            res = dp(i + direction, string[1], direction) if string[0] == s[i] else 0
            res += dp(i + direction, string, direction)
            return res % MOD
        res = 0
        digits = set(s)
        for mid in range(2, len(s) - 2):
            for d1, d2 in product(digits, digits):
                string = d1 + d2
                res += dp(mid - 1, string, -1) * dp(mid + 1, string, 1)
                res %= MOD
        return res

