from functools import cache

MOD = 10 ** 9 + 7

class Solution:
    def deleteString(self, s: str) -> int:
        def val(p):
            return ord(s[p]) - 97

        @cache
        def dp(start):
            if start == len(s):
                return 0
            if start + 1 == len(s):
                return 1
            p1 = start
            p2 = start
            hash1 = hash2 = 0
            res = 0
            power = 26
            while p2 + 1 < len(s):
                hash1 = (hash1 * 26 + val(p1)) % MOD
                hash2 = (hash2 * 26 * 26 + val(p2) * 26 + val(p2 + 1) - val(p1) * power) % MOD
                p1 += 1
                p2 += 2
                power *= 26
                power %= MOD
                if hash1 == hash2 and s[start:p1] == s[p1:p2]:
                    res = max(res, dp(p1))
                    if res == len(s) - p1:
                        break
            return res + 1
        return dp(0)

