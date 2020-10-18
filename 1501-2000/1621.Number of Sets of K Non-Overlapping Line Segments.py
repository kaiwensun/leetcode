from functools import lru_cache
MOD = 10 ** 9 + 7
class Solution:
    @lru_cache(None)
    def numberOfSets(self, n: int, k: int) -> int:
        if n < k + 1:
            return 0
        if k == 1:
            return n * (n - 1) // 2
        return (self.numberOfSetsCoveringEnd(n, k) + self.numberOfSets(n - 1, k)) % MOD
    @lru_cache(None)
    def numberOfSetsCoveringEnd(self, n: int, k: int) -> int:
        if n < k + 1:
            return 0
        if k == 1:
            return n - 1
        return (self.numberOfSets(n - 1, k - 1) + self.numberOfSetsCoveringEnd(n - 1, k)) % MOD

