from collections import defaultdict, Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        def get_slope(i, j):
            p1, p2 = sorted((points[i], points[j]))
            if p1[0] == p2[0]:
                return float("inf")
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

        point2slopes = defaultdict(Counter)
        
        res = 0
        for i in range(N):
            point2slopes = Counter()
            for j in range(i + 1, N):
                point2slopes[get_slope(i, j)] += 1
                res = max(res, max(point2slopes.values()))
        return res + 1

