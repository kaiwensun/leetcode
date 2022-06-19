from functools import cache

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        
        @cache
        def dp(m, n):
            if m == 0 or n == 0:
                return 0
            res = 0
            if (n, m) in wh2p:
                res = wh2p[n, m]
            for w in range(1, n // 2 + 1):
                res = max(res, dp(m, w) + dp(m, n - w))
            for h in range(1, m // 2 + 1):
                res = max(res, dp(h, n) + dp(m - h, n))
            return res
                
        wh2p = {}
        for h, w, p in prices:
            wh2p[w, h] = p
        return dp(m, n)

