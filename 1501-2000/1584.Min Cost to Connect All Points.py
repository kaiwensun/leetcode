class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        def calcDist(i, j):
            x, y = points[i]
            u, v = points[j]
            return abs(x - u) + abs(y - v)
        
        dists = []
        
        for i, (x, y) in enumerate(points):
            for j, (u, v) in enumerate(points):
                dists.append([calcDist(i, j), i, j])
        dists.sort()
        
        data = range(len(points))
        
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            xr = find(x)
            yr = find(y)
            if xr != yr:
                data[xr] = yr
            return xr != yr
        
        cost = 0
        for _, i, j in dists:
            if union(i, j):
                cost += calcDist(i, j)
        return cost

