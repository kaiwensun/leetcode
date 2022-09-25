from collections import defaultdict, Counter

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def build_graph(vals):
            graph = defaultdict(list)
            for u, v in edges:
                if vals[u] >= vals[v]:
                    graph[u].append(v)
                if vals[v] >= vals[u]:
                    graph[v].append(u)
            return graph

        def build_val_to_node(vals):
            val_to_node = defaultdict(list)
            for node, val in enumerate(vals):
                val_to_node[val].append(node)
            return val_to_node

        data = list(range(len(vals)))
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            data[rx] = ry

        graph = build_graph(vals)
        val_to_node = build_val_to_node(vals)

        res = 0
        for val in sorted(set(vals)):
            nodes = val_to_node[val]
            for node in nodes:
                for neighbor in graph[node]:
                    union(neighbor, node)
            counter = Counter(map(find, nodes))
            for cnt in counter.values():
                res += cnt * (cnt - 1) // 2
        return res + len(vals)

