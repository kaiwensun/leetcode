MOD = 10 ** 9 + 7

class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2, n, MOD) - 2) % MOD

