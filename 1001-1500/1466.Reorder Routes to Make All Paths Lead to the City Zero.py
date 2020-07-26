
import collections
class Solution(object):
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))
            graph[v].append((u, False))
        res = 0
        def dfs(node, prev):
            nonlocal res
            for neighbor, origin in graph[node]:
                if neighbor == prev:
                    continue
                if origin:
                    res += 1
                dfs(neighbor, node)
        dfs(0, None)
        return res
