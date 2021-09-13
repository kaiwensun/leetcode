class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res = prev = 0
        previ = -1
        for i, rate in enumerate(sorted([w / h for (w, h) in rectangles])):
            if rate != prev:
                prev = rate
                res += (i - previ - 1) * (i - previ) // 2
                previ = i
        i += 1
        res += (i - previ - 1) * (i - previ) // 2
        return res

