from collections import defaultdict, deque
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in xrange(n)]
        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    if i == j:
                        continue
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
        mn = n + 1
        res = None
        for start in xrange(n):
            count = len([d for d in dist[start] if d <= distanceThreshold])
            if count <= mn:
                mn = count
                res = start
        return res
