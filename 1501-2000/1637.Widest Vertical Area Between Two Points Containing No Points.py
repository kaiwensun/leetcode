class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xs = sorted(map(lambda p:p[0], points))
        return max(b - a for a, b in zip(xs[:-1], xs[1:]))

