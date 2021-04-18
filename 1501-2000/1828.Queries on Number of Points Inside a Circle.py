class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        return [
            sum((x - x2) ** 2 + (y - y2) ** 2 <= r ** 2 for x, y in points)
            for x2, y2, r in queries
        ]

