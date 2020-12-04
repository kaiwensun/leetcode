from functools import lru_cache
from collections import defaultdict

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        def make_graph(relation):
            graph = defaultdict(list)
            for src, dst in relation:
                graph[src].append(dst)
            return graph
        
        @lru_cache(None)
        def dp(player, step):
            if step == k:
                return int(player == n - 1)
            return sum(dp(next_player, step + 1) for next_player in graph[player])
        
        graph = make_graph(relation)
        return dp(0, 0)

