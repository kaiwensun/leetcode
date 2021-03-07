import heapq
import functools

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))
        
        distanceToLastNode = [None] * n
        # distanceToLastNode[-1] = 0
        heap = [(0, n - 1)]
        found = 0
        while found < n:
            dist, node = heapq.heappop(heap)
            if distanceToLastNode[node] is not None:
                continue
            found += 1
            distanceToLastNode[node] = dist
            for neighbor, w in graph[node]:
                heapq.heappush(heap, (dist + w, neighbor))
        
        @functools.lru_cache(None)
        def dfs(node):
            if node == n - 1:
                return 1
            res = 0
            for neighbor, _ in graph[node]:
                if distanceToLastNode[neighbor] < distanceToLastNode[node]:
                    res += dfs(neighbor)
            return res
        return dfs(0) % MOD

