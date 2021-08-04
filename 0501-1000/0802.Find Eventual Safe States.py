from collections import Counter, defaultdict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = []
        n = len(graph)
        rev_graph = defaultdict(list)
        safe = []
        readiness = Counter()
        for u, neighbors in enumerate(graph):
            for v in neighbors:
                rev_graph[v].append(u)
            if not neighbors:
                safe.append(u)
        safe_index = 0
        while safe_index < len(safe):
            v = safe[safe_index]
            safe_index += 1
            for u in rev_graph[v]:
                readiness[u] += 1
                if readiness[u] == len(graph[u]):
                    safe.append(u)
        return sorted(safe)

