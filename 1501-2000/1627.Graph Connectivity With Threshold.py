class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        data = range(n + 1)
        
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[max(rx, ry)] = min(rx, ry)
            return ry
        
        for divisor in xrange(threshold + 1, n + 1):
            if data[divisor] != divisor:
                continue
            for multiple in xrange(2, n + 1):
                if divisor * multiple > n:
                    break
                union(divisor, divisor * multiple)
        return [find(a) == find(b) for a, b in queries]

