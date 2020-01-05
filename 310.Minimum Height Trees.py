from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def makeGraph(edges, n):
            graph = [set() for _ in xrange(n)]
            for u, v in edges:
                graph[u].add(v)
                graph[v].add(u)
            return graph
        def getLeaves(graph, n):
            return [node for node in xrange(n) if len(graph[node]) <= 1]

        graph = makeGraph(edges, n)
        leaves = getLeaves(graph, n)
        depths = [0] * n
        queue = deque(leaves)
        res = []
        while queue:
            node = queue.popleft()
            if not graph[node]:
                res.append(node)
            for neighbor in graph[node]:
                graph[neighbor].discard(node)
                if len(graph[neighbor]) == 0:
                    if depths[neighbor] == depths[node]:
                        res.append(node)
                    depths[neighbor] = depths[node] + 1
                elif len(graph[neighbor]) == 1:
                    queue.append(neighbor)
                    depths[neighbor] = depths[node] + 1
        return res
