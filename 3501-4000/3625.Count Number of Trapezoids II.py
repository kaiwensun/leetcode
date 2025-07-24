from collections import Counter, defaultdict
from math import inf

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        def get_slope(p1, p2):
            if p1[0] == p2[0]:
                return inf
            if p1[1] == p2[1]:
                return 0
            p1, p2 = sorted([p1, p2])
            return round((p1[1] - p2[1]) / (p1[0] - p2[0]), 10)

        slope_to_intercept_to_cnt = defaultdict(Counter)
        # Deduplicate parallelograms. A parallelogram is found if two edges have the same slope and same length, but different intercept
        slope_len_to_intercept_to_cnt = defaultdict(Counter)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                slope = get_slope(p1, p2)
                if slope == inf:
                    intercept = p1[0]
                elif slope == 0:
                    intercept = p1[1]
                else:
                    intercept = round(p2[0] - (p2[0] - p1[0]) / (p2[1] - p1[1]) * p2[1], 10)
                slope_to_intercept_to_cnt[slope][intercept] += 1
                length = abs(p2[1] - p1[1]) if slope == inf else abs(p2[0] - p1[0])
                slope_len_to_intercept_to_cnt[slope, length][intercept] += 1

        res = 0
        for slope, group in slope_to_intercept_to_cnt.items():
            prev = 0
            for intercept, cnt in group.items():
                res += cnt * prev
                prev += cnt

        parallelogram_cnt = 0
        for slope_len, intercept_to_cnt in slope_len_to_intercept_to_cnt.items():
            prev = 0
            for intercept, cnt in intercept_to_cnt.items():
                parallelogram_cnt += cnt * prev
                prev += cnt
        return res - parallelogram_cnt // 2

