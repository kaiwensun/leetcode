from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost = defaultdict(lambda: float("inf"))
        for l in ascii_lowercase:
            min_cost[l, l] = 0
        for f, t, c in zip(original, changed, cost):
            min_cost[f, t] = min(min_cost[f, t], c)
        for k in ascii_lowercase:
            for i in ascii_lowercase:
                for j in ascii_lowercase:
                    min_cost[i, j] = min(min_cost[i, j], min_cost[i, k] + min_cost[k, j])
        res = sum(min_cost[i, j] for i, j in zip(source, target))
        return -1 if res == float("inf") else res
