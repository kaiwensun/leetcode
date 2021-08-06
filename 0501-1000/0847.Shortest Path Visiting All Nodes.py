class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        res = 0
        seen = set()
        queue = deque([(1 << start, start) for start in range(n)])
        queue.append(("#", "#"))
        while True:
            visited, last = queue.popleft()
            if visited == "#":
                res += 1
                queue.append(("#", "#"))
                continue
            for nxt in graph[last]:
                key = (visited | (1 << nxt), nxt)
                if key[0] == (1 << n) - 1:
                    return res + 1
                if key not in seen:
                    seen.add(key)
                    queue.append(key)

