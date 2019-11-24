class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        return sum(max(abs(src[0] - dst[0]), abs(src[1] - dst[1])) for src, dst in zip(points[:-1], points[1:]))
