from functools import lru_cache

MOD = 10 ** 9 + 7

@lru_cache(None)
def dp(n, k):
    if n == k:
        return 1
    if k == 0:
        return 0
    return (dp(n - 1, k - 1) + (n - 1) * dp(n - 1, k)) % MOD

class Solution:
    @lru_cache(None)
    def rearrangeSticks(self, n: int, k: int) -> int:
        return dp(n, k)

