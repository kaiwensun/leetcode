from functools import cache
from collections import defaultdict


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        couple_heads = set()
        graph = defaultdict(set)
        for a, b in enumerate(favorite):
            if favorite[b] != a:
                graph[b].add(a)
            elif a < b:
                couple_heads.add(a)
        N = len(favorite)
        res = 0

        def dfs_fans(node):
            res = 0
            for fan in graph[node]:
                res = max(res, dfs_fans(fan))
            return 1 + res

        for a in couple_heads:
            b = favorite[a]
            res += dfs_fans(a) + dfs_fans(b)

        ranks = [None] * N
        def look_for_cycles(node, start_rank):
            cur = node
            rank = start_rank
            while ranks[cur] is None:
                ranks[cur] = rank
                rank += 1
                cur = favorite[cur]
            if ranks[cur] < start_rank:
                return float("-inf"), rank
            else:
                return rank - ranks[cur], rank

        start_rank = 0
        for node in range(N):
            rtn = look_for_cycles(node, start_rank)
            res = max(res, rtn[0])
            start_rank = rtn[1]
        return res

