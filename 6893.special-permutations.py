from collections import defaultdict
from functools import cache

MOD = 10 ** 9 + 7

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    graph[i].append(j)
                    graph[j].append(i)
        if len(graph) != len(nums):
            return 0
        all_selected = (1 << len(nums)) - 1
        @cache
        def dp(prev, bitmap):
            if bitmap == all_selected:
                return 1
            res = 0
            for nxt in graph[prev]:
                if bitmap & (1 << nxt) == 0:
                    res += dp(nxt, bitmap | (1 << nxt))
                    res %= MOD
            return res
        return sum(dp(i, 1 << i) for i in range(len(nums))) % MOD

