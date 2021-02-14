import collections
class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """ 
        graph = collections.defaultdict(set)
        node_degree = [0] * n
        for u, v in edges:
            graph[min(u, v) - 1].add(max(u, v) - 1)
            node_degree[u - 1] += 1
            node_degree[v - 1] += 1
        res = float("inf")
        for x in xrange(n):
            for y in graph[x]:
                for z in graph[x] & graph[y]:
                    res = min(res, node_degree[x] + node_degree[y] + node_degree[z])
        return -1 if res == float("inf") else res - 6

