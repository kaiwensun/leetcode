import collections, functools, math

MOD = 10 ** 9 + 7

@lru_cache(None)
def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1) % MOD

@lru_cache(None)
def inv_fact(num):
    return pow(fact(num), MOD - 2, MOD)

class Solution:
    def makeStringSorted(self, s: str) -> int:

        cnt = collections.Counter(s)
        res = 0

        for i in range(len(s)):
            duplicate_size = sum(value for key, value in cnt.items() if key < s[i]) * fact(len(s) - i - 1) % MOD
            res += functools.reduce(lambda prod, num: prod * inv_fact(num) % MOD, cnt.values(), duplicate_size)
            res %= MOD
            cnt[s[i]] -= 1
        return res

