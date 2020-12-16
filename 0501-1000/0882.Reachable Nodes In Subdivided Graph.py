class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, n in edges:
            graph[u].append((v, n))
            graph[v].append((u, n))
        internal_counts = {tuple(sorted((u, v))):n for u, v, n in edges}
        res = 0
        queue = [(-M, 0)]
        visited = [False] * N
        while queue:
            fule, node = heapq.heappop(queue)
            fule = -fule
            if visited[node]:
                continue
            visited[node] = True
            res += 1
            for neighbor, dist in graph[node]:
                edge_name = tuple(sorted((node, neighbor)))
                taken = min(internal_counts[edge_name], fule)
                res += taken
                internal_counts[edge_name] -= taken
                if dist + 1 <= fule and not visited[neighbor]:
                    heapq.heappush(queue, (-(fule - dist - 1), neighbor))
        return res

