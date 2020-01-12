class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        data = range(n)
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            xp = find(x)
            yp = find(y)
            if xp != yp:
                data[xp] = yp
        for conn in connections:
            union(conn[0], conn[1])
        for x in xrange(n):
            find(x)
        return len(set(data)) - 1
