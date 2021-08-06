class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        res = float("inf")
        seen = defaultdict(lambda: float("inf"))
        for start in range(n):
            queue = deque([(1 << start, start, 0)])
            while queue:
                visited, last, dist = queue.popleft()
                if visited == (1 << n) - 1:
                    res = min(res, dist)
                if seen[(visited, last)] > dist:
                    seen[(visited, last)] = dist
                    for nxt in graph[last]:
                        queue.append((visited | (1 << nxt), nxt, dist + 1))
        return res

