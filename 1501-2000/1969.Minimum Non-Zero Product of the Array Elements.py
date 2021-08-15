MOD = 10 ** 9 + 7

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        all_1s = (1 << p) - 1
        return (pow(all_1s - 1, all_1s >> 1, MOD) * all_1s) % MOD

