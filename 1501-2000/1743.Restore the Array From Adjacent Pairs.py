from collections import defaultdict
class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(set)
        for u, v in adjacentPairs:
            graph[u].add(v)
            graph[v].add(u)
        for a, b in graph.iteritems():
            if len(b) == 1:
                break
        res = [a]
        while graph[a]:
            b = graph[a].pop()
            res.append(b)
            graph[b].remove(a)
            a = b
        return res

