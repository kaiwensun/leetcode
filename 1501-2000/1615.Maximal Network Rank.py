from collections import defaultdict
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        res = 0
        for u in xrange(n):
            for v in xrange(u + 1, n):
                if v in graph[u]:
                    res = max(res, len(graph[u]) + len(graph[v]) - 1)
                else:
                    res = max(res, len(graph[u]) + len(graph[v]))
        return res

