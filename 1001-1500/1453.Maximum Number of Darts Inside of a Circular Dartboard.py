import math
import collections
class Solution(object):
    def numPoints(self, points, r):
        """
        :type points: List[List[int]]
        :type r: int
        :rtype: int
        """
        d = r * 2
        r2 = r * r
        neighbors = collections.defaultdict(list)
        for index, point in enumerate(points):
            for other_index in xrange(index + 1, len(points)):
                other_point = points[other_index]
                if (point[0] - other_point[0]) ** 2 + (point[1] - other_point[1]) ** 2 <= d ** 2:
                    neighbors[index].append(other_index)
                    neighbors[other_index].append(index)
        res = 1 if points else 0
        for host in xrange(len(points)):
            for snd_host in neighbors[host]:
                host_point = points[host]
                snd_host_point = points[snd_host]
                base = ((snd_host_point[0] - host_point[0]) / 2.0, (snd_host_point[1] - host_point[1]) / 2.0)
                sizeSquare = base[0] ** 2 + base[1] ** 2
                size = math.sqrt(sizeSquare)
                unitBase = (base[0] / size, base[1] / size)
                rectSize = math.sqrt(r2 - sizeSquare)
                for unitRectBase in ((-unitBase[1], unitBase[0]), (unitBase[1], -unitBase[0])):
                    rectBase = (rectSize * unitRectBase[0], rectSize * unitRectBase[1])
                    center = (host_point[0] + base[0] + rectBase[0], host_point[1] + base[1] + rectBase[1])
                    cnt = 0
                    for point_index in neighbors[host]:
                        point = points[point_index]
                        if r2 + 1e-5 >= (center[0] - point[0]) ** 2 + (center[1] - point[1]) ** 2:
                            cnt += 1
                    res = max(res, cnt + 1)
        return res
