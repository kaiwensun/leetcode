import collections
class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        def dfs(node, cost):
            if cost > t:
                return None
            if node == target:
                if graph[node]:
                    if cost != t:
                        return 0.0
                    else:
                        return 1.0
                else:
                    return 1.0
            else:
                for neighbor in graph[node]:
                    graph[neighbor].discard(node)
                    res = dfs(neighbor, cost + 1)
                    if res is not None:
                        return res / len(graph[node])
                return None
        return dfs(1, 0) or 0
