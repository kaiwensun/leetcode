from collections import defaultdict
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(dict)
        for u, v, cost in edges:
            self.graph[u][v] = cost

    def addEdge(self, edge: List[int]) -> None:
        u, v, cost = edge
        self.graph[u][v] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        queue = [[0, node1]]
        dist = {}
        while queue:
            d, node = heapq.heappop(queue)
            if node == node2:
                return d
            if node in dist:
                continue
            dist[node] = d
            for nxt, d in self.graph[node].items():
                if nxt in dist:
                    continue
                heapq.heappush(queue, [dist[node] + d, nxt])
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

