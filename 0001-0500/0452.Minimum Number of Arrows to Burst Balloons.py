class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda point:point[1])
        res, cur = 0, float("-inf")
        for start, end in points:
            if start > cur:
                cur = end
                res += 1
        return res

