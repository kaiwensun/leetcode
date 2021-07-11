from functools import cache

MOD = 10 ** 9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache
        def dp(i, j, up, left):
            if i == n:
                return 1
            res = 0
            for color in range(3):
                if left[j] == color or up == color:
                    continue
                res += dp(i + (j + 1) // m, (j + 1) % m, 4 if j + 1 == m else color, left[:j] + (color,) + left[j + 1:])
                res %= MOD
            return res
        return dp(0, 0, 4, (4,) * m)

