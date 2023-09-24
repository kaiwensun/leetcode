class Solution:
    def cuttingRope(self, n: int) -> int:

        @lru_cache(None)
        def dp(n):
            if n == 1:
                return 1
            res = n
            for cur in range(1, n):
                res = max(res, cur * dp(n - cur))
            return res
        return max(dp(n - i) * dp(i) for i in range(1, n))

