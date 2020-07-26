class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        def pointInRect(x, y):
            return x1 <= x <= x2 and y1 <= y <= y2
        def pointInCircle(x, y):
            return (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2
        def edgeCutsCircle(edge):
            (x1, y1), (x2, y2) = edge
            if x1 == x2:
                return abs(x1 - x_center) <= radius and (pointInCircle(x1, y1) or pointInCircle(x2, y2) or (y1 < y_center) != (y2 < y_center))
            else:
                return abs(y1 - y_center) <= radius and (pointInCircle(x1, y1) or pointInCircle(x2, y2) or (x1 < x_center) != (x2 < x_center))
        edges = (
            ((x1, y1), (x1, y2)),
            ((x1, y2), (x2, y2)),
            ((x2, y2), (x2, y1)),
            ((x2, y1), (x1, y1))
        )
        return pointInCircle((x1 + x2) / float(2), (y1 + y2) / float(2)) or pointInRect(x_center, y_center) or any(map(edgeCutsCircle, edges))
