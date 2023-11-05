from functools import cache
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        @cache
        def dp(node, parent, ancestors_all_zero):
            if len(graph[node]) == 1 and node != 0:
                return 0 if ancestors_all_zero else values[node]
            res = 0
            for child in graph[node]:
                if child == parent:
                    continue
                res += dp(child, node, False)
            if not ancestors_all_zero:
                return res + values[node]
            res2 = values[node]
            for child in graph[node]:
                if child == parent:
                    continue
                res2 += dp(child, node, True)
            return max(res, res2)
        return dp(0, -1, True)
