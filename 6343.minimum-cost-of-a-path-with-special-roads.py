import collections, heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def euclidean_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        def get_distance(p1, p2):
            return distances[p1].get(p2, euclidean_distance(p1, p2))
        start, target = tuple(start), tuple(target)
        if start == target:
            return 0
        points = {start, target}
        distances = collections.defaultdict(dict)
        for x1, y1, x2, y2, cost in specialRoads:
            p1, p2 = (x1, y1), (x2, y2)
            if cost < get_distance(p1, p2):
                distances[p1][p2] = cost
            points.add(p1)
            points.add(p2)
        heap = [(0, start)]
        visited = set()
        while heap:
            cost, p = heapq.heappop(heap)
            if p == target:
                return cost
            if p in visited:
                continue
            visited.add(p)
            for np in list(points):
                new_cost = cost + get_distance(p, np)
                heapq.heappush(heap, (new_cost, np))
        return -1

