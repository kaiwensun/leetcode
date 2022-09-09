from functools import cache

MOD = 10 ** 9 + 7

@cache
def dp(i, k):
    if abs(i) > k:
        return 0
    if k == 0:
        return 1
    return (dp(i + 1, k - 1) + dp(i - 1, k - 1)) % MOD
    

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        endPos -= startPos
        if endPos % 2 != k % 2:
            return 0
        return dp(abs(endPos), k)

