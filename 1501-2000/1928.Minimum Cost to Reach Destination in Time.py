from collections import defaultdict
import heapq

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        N = len(passingFees)
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for u, v, t in edges:
            if t <= maxTime:
                graph[v][u] = graph[u][v] = min(graph[u][v], t)

        visited = set()  # [(node, total_spent_time)]
        queue = [(passingFees[0], 0, 0)]  # [(total_fee, node, total_spent_time)]
        while queue:
            fee, u, t = heapq.heappop(queue)
            if (u, t) in visited:
                continue
            visited.add((u, t))
            for v, dt in graph[u].items():
                if (v, t + dt) in visited or t + dt > maxTime:
                    continue
                if v == N - 1:
                    return fee + passingFees[v]
                heapq.heappush(queue, (fee + passingFees[v], v, t + dt))
        return -1

