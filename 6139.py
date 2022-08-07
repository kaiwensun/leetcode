from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(list)
        for u, v in edges:
            if u in restricted or v in restricted:
                continue
            graph[u].append(v)
            graph[v].append(u)
        def dfs(root, prev):
            res = 1
            for nxt in graph[root]:
                if nxt == prev:
                    continue
                res += dfs(nxt, root)
            return res
        return dfs(0, 0)

