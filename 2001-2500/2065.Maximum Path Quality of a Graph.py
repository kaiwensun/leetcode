from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))

        def dfs(start, visited, remainTime):
            if remainTime < 0:
                assert(False)
            res = 0 if start == 0 else float("-inf")
            start_was_visited = start in visited
            visited.add(start)
            node_value = 0 if start_was_visited else values[start]
            for nxt, t in graph[start]:
                if t > remainTime:
                    continue
                res = max(res, node_value + dfs(nxt, visited, remainTime - t))
            if not start_was_visited:
                visited.remove(start)
            return res

        return dfs(0, {0}, maxTime) + values[0]

