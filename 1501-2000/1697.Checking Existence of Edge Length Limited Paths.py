class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        sorted_queries = []
        for i in xrange(len(queries)):
            p, q, limit = queries[i]
            sorted_queries.append((limit, p, q, i))
        sorted_queries.sort()
        sorted_edges = []
        queries.sort(key=lambda q:q[-1])
        sorted_edges = list(sorted(edgeList, key=lambda e:e[-1]))
        
        data = {i:i for i in xrange(n)}
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry
        res = []
        edge_ptr = 0
        for limit, p, q, i in sorted_queries:
            while edge_ptr < len(sorted_edges) and sorted_edges[edge_ptr][-1] < limit:
                union(sorted_edges[edge_ptr][0], sorted_edges[edge_ptr][1])
                edge_ptr += 1
            res.append((i, find(p) == find(q)))
        return [item[1]  for item in sorted(res)]

