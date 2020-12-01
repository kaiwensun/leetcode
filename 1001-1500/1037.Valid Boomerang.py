class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        def get_length(point1, point2):
            return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        lengths = list(sorted(get_length(points[i], points[i + 1]) for i in xrange(-1, 2)))
        if lengths[0] == 0:
            return False
        if abs(lengths[0] + lengths[1] - lengths[2]) < 1e-6:
            return False
        return True

