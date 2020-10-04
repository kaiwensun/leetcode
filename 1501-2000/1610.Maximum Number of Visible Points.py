import collections
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        for point in points:
            point[0] -= location[0]
            point[1] -= location[1]
        total_size = len(points)
        view = math.radians(angle)
        points = [point for point in points if point[0] != 0 or point[1] != 0]
        center = total_size - len(points)
        angles = sorted([math.atan2(y, x) for x, y in points])
        angles += [math.pi * 2 + angle for angle in angles]
        window = collections.deque()
        res = 0
        for angle in angles:
            window.append(angle)
            while window[-1] - window[0] > view:
                window.popleft()
            res = max(res, len(window))
        return res + center

