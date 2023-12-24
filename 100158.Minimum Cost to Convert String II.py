from collections import defaultdict
from functools import cache

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost = defaultdict(lambda: float("inf"))
        def get_dist(s1, s2):
            if s1 == s2:
                return 0
            return min_cost[s1, s2]
        def set_dist(s1, s2, dist):
            min_cost[s1, s2] = min(get_dist(s1, s2), dist)
        for f, t, c in zip(original, changed, cost):
            set_dist(f, t, c)
        all_states = list(set(original) | set(changed))
        groups = defaultdict(list)
        for s in all_states:
            groups[len(s)].append(s)
        for states in groups.values():
            states = list(states)
            for k in states:
                for i in states:
                    for j in states:
                        set_dist(i, j, get_dist(i, k) + get_dist(k, j))
        lengths = sorted(set(groups.keys()) | {1})

        @cache
        def dp(j):
            if j == 0:
                return 0
            res = float("inf")
            for l in lengths:
                if l > j:
                    break
                key = (source[j - l:j], target[j - l:j])
                cur = get_dist(source[j - l:j], target[j - l:j])
                if cur != float("inf"):
                    res = min(res, cur + dp(j - l))
            return res
        res = dp(len(source))
        return -1 if res == float("inf") else res

