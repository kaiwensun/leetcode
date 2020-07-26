import collections, heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        if start == end:
            return 1.0
        visited = set()
        graph = collections.defaultdict(list)
        for i in xrange(len(edges)):
            u, v = edges[i]
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])
        heap = [[-1.0, start]]
        while heap:
            neg_prob, node = heapq.heappop(heap)
            if node == end:
                return -neg_prob
            if node in visited:
                continue
            visited.add(node)
            for neighbor, edge_prob in graph[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(heap, [edge_prob * neg_prob, neighbor])
        return 0.0
