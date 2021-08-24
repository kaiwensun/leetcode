import heapq, collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        graph = collections.defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))

        queue = [(0, src, 0)]
        visited = set()
        while queue:
            cost, u, steps = heapq.heappop(queue)
            if u == dst:
                return cost
            if steps == k + 1:
                continue
            for v, cost_inc in graph[u]:
                item = (cost + cost_inc, v, steps + 1)
                if item in visited: 
                    continue
                visited.add(item)
                heapq.heappush(queue, item)
        return -1

