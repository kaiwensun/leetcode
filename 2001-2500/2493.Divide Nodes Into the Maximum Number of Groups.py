from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def make_graph(edges):
            graph = defaultdict(list)
            for a, b in edges:
                a -= 1
                b -= 1
                graph[a].append(b)
                graph[b].append(a)
            return graph

        def get_connected_components(graph):
            visited = [False] * n
            components = []
            def dfs(node, parent, collector):
                if visited[node]:
                    return collector
                collector.add(node)
                visited[node] = True
                for neighbor in graph[node]:
                    dfs(neighbor, node, collector)
                return collector
            for node in range(n):
                if not visited[node]:
                    components.append(dfs(node, -1, set()))
            return components

        def bfs(start):
            res = 0
            visited = set()
            queue = {start}
            while queue:
                res += 1
                next_queue = set()
                for cur_node in queue:
                    visited.add(cur_node)
                    for next_node in graph[cur_node]:
                        if next_node in queue:
                            return -1
                        if next_node in visited:
                            continue
                        next_queue.add(next_node)
                queue = next_queue
            return res

        graph = make_graph(edges)
        components = get_connected_components(graph)
        res = 0
        for component in components:
            component_best = -1
            for start in component:
                component_best = max(component_best, bfs(start))
                if component_best == -1:
                    return -1
            res += component_best
        return res

