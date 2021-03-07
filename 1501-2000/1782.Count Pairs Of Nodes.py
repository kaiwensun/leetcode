from collections import Counter
class Solution(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        degrees = [0] * n
        graph = [Counter() for _ in xrange(n)]
        for u, v in edges:
            graph[u - 1][v - 1] += 1
            graph[v - 1][u - 1] += 1
            degrees[u - 1] += 1
            degrees[v - 1] += 1

        sorted_degrees = sorted((degree, node) for node, degree in enumerate(degrees))
        node2index = [None] * n
        for index, (_, node) in enumerate(sorted_degrees):
            node2index[node] = index
        
        def handle_query(query):
            res = 0
            for node in xrange(n):
                pivot = bisect.bisect_right(sorted_degrees, (query - degrees[node], float("inf")))
                res += n - pivot
                for neighbor in graph[node]:
                    if node2index[neighbor] >= pivot:
                        if degrees[node] + degrees[neighbor] - graph[node][neighbor] <= query:
                            res -= 1
                if node2index[node] >= pivot:
                    res -= 1
            return res // 2
        
        return map(handle_query, queries)

