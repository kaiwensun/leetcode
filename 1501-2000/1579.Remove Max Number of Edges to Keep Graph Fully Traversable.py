from collections import defaultdict
class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(x, data):
            if data[x] != x:
                data[x] = find(data[x], data)
            return data[x]
        def union(x, y, data):
            px = find(x, data)
            py = find(y, data)
            if px != py:
                data[px] = py
                return True
            return False
        
        graphs = [[] for _ in xrange(3)]
        for typ, u, v in edges:
            graphs[typ - 1].append((u - 1, v - 1))
        both = range(n)
        use = 0
        for u, v in graphs[2]:
            use += union(u, v, both)
        alice, bob = list(both), both
        for u, v in graphs[0]:
            use += union(u, v, alice)
        for u, v in graphs[1]:
            use += union(u, v, bob)
        if 1 == len(set(find(u, alice) for u in xrange(n))) == len(set(find(u, bob) for u in xrange(n))):
            return len(edges) - use
        else:
            return -1

