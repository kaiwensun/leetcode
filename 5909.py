from functools import cache
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        pres = defaultdict(list)
        for pre, nxt in relations:
            pres[nxt - 1].append(pre - 1)

        @cache
        def dp(cur):
            res = 0
            for pre in pres[cur]:
                res = max(res, dp(pre))
            return res + time[cur]

        return max(dp(cur) for cur in range(n))

