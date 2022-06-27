from functools import cache

MOD = 10 ** 9 + 7
ALLOW = [
    list(range(1, 7)),
    list(range(1, 7)),
    [1, 3, 5],
    [1, 2, 4, 5],
    [1, 3, 5],
    [1, 2, 3, 4, 6],
    [1, 5]
]

@cache
def dp(a, b, k):
    if k == 0:
        return 1
    res = 0
    for c in ALLOW[b]:
        if c != a and c != b:
            res += dp(b, c, k - 1)
    return res % MOD

class Solution:
    def distinctSequences(self, n: int) -> int:
        return dp(0, 0, n)

