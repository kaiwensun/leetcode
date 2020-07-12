import collections
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
        probs = [None] * n
        # probs[start] = 1.0
        graph = collections.defaultdict(list)
        for i in xrange(len(edges)):
            u, v = edges[i]
            graph[u].append([v, succProb[i]])
            graph[v].append([u, succProb[i]])
        priority_queue = collections.defaultdict(float)
        priority_queue[start] = 1.0
        def findMax(priority_queue):
            max_prob = -1
            res = None
            for node, prob in priority_queue.iteritems():
                if max_prob < prob:
                    max_prob = prob
                    res = node
            return res
        
        while priority_queue:
            node = findMax(priority_queue)
            probs[node] = priority_queue.pop(node)
            if node == end:
                return probs[node]
            for neighbor, edge_prob in graph[node]:
                if probs[neighbor] is not None:
                    continue                
                priority_queue[neighbor] = max(priority_queue[neighbor], probs[node] * edge_prob)
        return 0.0
