from functools import cache

MOD = 10 ** 9 + 7

@cache
def prefix_sum(i, k):
    if i == 0:
        return 1
    return (value(i, k) + prefix_sum(i - 1, k)) % MOD

@cache
def value(i, k):
    if i == 0 or k == 0:
        return 1
    return (value(i, k - 1) + prefix_sum(i - 1, k - 1)) % MOD

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        return value(n - 1, k)

