from functools import cache
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter()
        for p in power:
            cnt[p] += p
        power_keys = sorted(cnt.keys())

        @cache
        def dp(i):
            if i >= len(power_keys):
                return 0
            res = cnt[power_keys[i]]
            for j in range(i + 1, min(i + 4, len(power_keys))):
                if power_keys[i] + 2 < power_keys[j]:
                    res += dp(j)
                    break
            res = max(res, dp(i + 1))
            return res
        return dp(0)

