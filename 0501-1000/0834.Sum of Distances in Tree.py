from collections import defaultdict
from functools import lru_cache

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:

        @lru_cache(None)
        def get_sum_and_count(node, parent):
            sm = cnt = 0
            for child in graph[node]:
                if child != parent:
                    s, c = get_sum_and_count(child, node)
                    sm += s + c
                    cnt += c
            return sm, cnt + 1
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return [get_sum_and_count(node, None)[0] for node in range(N)]

