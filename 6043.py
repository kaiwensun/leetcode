from collections import defaultdict
from bisect import bisect_left

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rects = defaultdict(list)
        for l, h in rectangles:
            rects[h].append(l)
        for value in rects.values():
            value.sort()
        heights = sorted(rects.keys(), reverse=True)
        def count(x, y):
            res = 0
            for h in heights:
                if h < y:
                    break
                res += len(rects[h]) - bisect_left(rects[h], x)
            return res
        return [count(x, y) for (x, y) in points]

