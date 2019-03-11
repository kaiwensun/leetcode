class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        min_area = float('inf')
        mapping = self.grouping(points)
        for key, point1s in mapping.iteritems():
            if len(point1s) == 1:
                continue
            left, right = self.getMinAreaPoints(point1s, key[0])
            area = math.sqrt(self.distanceSq(left, right)) * math.sqrt(key[2])
            min_area = min(min_area, area)
        return 0 if min_area == float('inf') else min_area

    def getMinAreaPoints(self, points, slop):
        points = sorted(points)
        min_diff = float('inf')
        rval = (None, None)
        compared_dimen = 0 if slop else 1
        for i in xrange(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            if min_diff >  p2[compared_dimen] - p1[compared_dimen]:
                min_diff = p2[compared_dimen] - p1[compared_dimen]
                rval = p1, p2
        return rval

    def grouping(self, points):
        points = [(x, y) for (x, y) in sorted(points)]
        mapping = {}
        for i in xrange(len(points)):
            for j in xrange(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                if self.isInteresting(p1, p2):
                    key = self.getKey(p1, p2)
                    mapping.setdefault(key, set()).add(p1)
        return mapping
                
        
    def isInteresting(self, p1, p2):
        return p1[0] < p2[0] and p1[1] <= p2[1]

    def getKey(self, p1, p2):
        s = self.slop(p1, p2)
        i = self.intercept(p1, s) if s else p1[0]
        d = self.distanceSq(p1, p2)
        return (self.blur(s), self.blur(i), self.blur(d))
    
    def slop(self, p1, p2):
        return (p2[1] - p1[1]) / float(p2[0] - p1[0])
    
    def intercept(self, p1, slop):
        if slop == 0:
            return p1[1]
        return p1[1] + p1[0] / float(slop)
    
    
    def distanceSq(self, p1, p2):
        return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2
    
    def blur(self, num):
        return int(num * 100000) / float(100000)
        
    # only look at edges whose direction is in the first quadrant (including x-axis direction). construct a mapping from (slop, cut y axis at for the another edge left point, distance^2) => point1 for all pairs of points
    
    
