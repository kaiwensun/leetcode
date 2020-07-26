class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [None] * N
        colors = range(1, 5)
        edges = collections.defaultdict(list)
        for u, v in paths:
            edges[u - 1].append(v - 1)
            edges[v - 1].append(u - 1)
        for node in xrange(N):
            neighbor_colors = tuple(res[n] for n in edges[node])
            for color in colors:
                if color not in neighbor_colors:
                    res[node] = color
                    break
        return res
