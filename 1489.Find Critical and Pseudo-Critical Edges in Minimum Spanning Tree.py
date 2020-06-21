from collections import defaultdict
class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        critical = set()
        pseudo_critical = set()
        edge_bucket = defaultdict(list)
        
        connectedComponent = range(n)
        
        def find(x, data=connectedComponent):
            if data[x] != x:
                data[x] = find(data[x], data)
            return data[x]
        def union(x, y, data=connectedComponent):
            rx = find(x, data)
            ry = find(y, data)
            if rx != ry:
                data[rx] = ry

        def dfs(cc, through, rank, ranks):
            seen_edges.add(through)
            if cc in ranks:
                return ranks[cc]
            ranks[cc] = rank
            for neighbor, edge_index in graph[cc]:
                if edge_index in seen_edges:
                    continue
                back_rank = dfs(neighbor, edge_index, rank + 1, ranks)
                if back_rank <= rank:
                    pseudo_critical.add(edge_index)
                else:
                    critical.add(edge_index)
                ranks[cc] = min(ranks[cc], back_rank)
            return ranks[cc]

        for index, edge in enumerate(edges):
            edge_bucket[edge[2]].append(index)

        for weight in sorted(edge_bucket.keys()):
            edge_indexes = edge_bucket[weight]
            graph = defaultdict(list)
            for edge_index in edge_indexes:
                u, v, _ = edges[edge_index]
                ru = find(u)
                rv = find(v)
                if ru == rv:
                    continue
                graph[find(u)].append([find(v), edge_index])
                graph[find(v)].append([find(u), edge_index])
            seen_edges = set()
            for cc, neighbors in graph.iteritems():
                dfs(cc, None, 0, {})
            for edge_index in edge_indexes:
                u, v, _ = edges[edge_index]
                union(u, v)

        return [list(critical), list(pseudo_critical)]
                
