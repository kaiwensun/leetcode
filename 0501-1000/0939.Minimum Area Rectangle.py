class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        point_set = set(map(tuple, points))
        for point in points:
            cols[point[0]].append(point)
            rows[point[1]].append(point)
        res = float('inf')
        for topleft in points:
            topright_x = [tr[0] for tr in rows[topleft[1]] if tr[0] > topleft[0]]
            bottomleft_y = [bl[1] for bl in cols[topleft[0]] if bl[1] < topleft[1]]
            for x in topright_x:
                for y in bottomleft_y:
                    if (x, y) in point_set:
                        res = min(res, (x - topleft[0]) * (topleft[1] - y))
        return res if res != float('inf') else 0
