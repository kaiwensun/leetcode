from collections import defaultdict
import heapq

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def deduplicate_edges(edges):
            fromto_2_weight = defaultdict(lambda: float("inf"))
            for u, v, w in edges:
                fromto_2_weight[(u, v)] = min(fromto_2_weight[(u, v)], w)
            return [(u, v, fromto_2_weight[(u, v)]) for (u, v) in fromto_2_weight]

        def dijkstra(total_cost, queue):
            while queue:
                cost, u = heapq.heappop(queue)
                for v, w in graph[u]:
                    if total_cost.get(v, float("inf")) > cost + w:
                        heapq.heappush(queue, (cost + w, v))
                        total_cost[v] = cost + w
            return total_cost

        edges = deduplicate_edges(edges)
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])

        cost1 = dijkstra({src1: 0}, [(0, src1)])
        cost2 = dijkstra({src2: 0}, [(0, src2)])
        if dest not in cost1 or dest not in cost2:
            return -1
        queue3 = [(cost1[node] + cost2[node], node) for node in cost1 if node in cost2]
        heapq.heapify(queue3)
        cost3 = dijkstra({}, queue3)
        return min(cost3.get(dest, float("inf")), cost1[dest] + cost2[dest])

