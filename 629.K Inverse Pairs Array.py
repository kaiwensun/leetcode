import functools

class Solution:
    MOD = 10 ** 9 + 7
    @functools.lru_cache(None)
    def kInversePairs(self, n: int, k: int) -> int:
        if k == 0:
            return 1
        if n == 1 or k < 0:
            return 0
        if (n - 1) * n < k * 2:
            return 0
        if k - n < 0:
            return (self.kInversePairs(n - 1, k) + self.kInversePairs(n, k - 1)) % self.MOD
        else:
            return (self.kInversePairs(n - 1, k) + self.kInversePairs(n, k - 1) - self.kInversePairs(n - 1, k - n)) % self.MOD
