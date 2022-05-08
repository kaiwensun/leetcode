from functools import cache

MOD = 10 ** 9 + 7

@cache
def dp(keys, length):
    if length == 0:
        return 1
    res = 0
    for i in range(1, min(length, keys) + 1):
        res += dp(keys, length - i)
    return res % MOD

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        def count():
            token = ""
            cnt = 0
            for s in pressedKeys + " ":
                if s != token:
                    if token:
                        if token in "79":
                            yield 4, cnt
                        else:
                            yield 3, cnt
                    token = s
                    cnt = 1
                else:
                    cnt += 1

        res = 1
        for keys, repeat in count():
            res *= dp(keys, repeat)
            res %= MOD
        return res % MOD

