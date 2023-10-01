from collections import defaultdict
from functools import cache

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        sources = set(range(n))
        for u, v in enumerate(edges):
            if v in sources:
                sources.remove(v)
        answer = [None] * n
        ranks = [None] * n
        def dfs(node, rank):
            if answer[node] is not None:
                return None, None, answer[node] + 1
            if ranks[node] is not None:
                return ranks[node], rank, None
            ranks[node] = rank
            joint_rank, highest_rank, res = dfs(edges[node], rank + 1)
            if res is None:
                answer[node] = highest_rank - min(rank, joint_rank)
                if rank == joint_rank:
                    return None, None, answer[node] + 1
                else:
                    return joint_rank, highest_rank, None
            else:
                answer[node] = res
                return None, None, res + 1
        for source in sources:
            dfs(source, 0)
        for node in range(n):
            if answer[node] is None:
                dfs(node, 0)
        return answer

