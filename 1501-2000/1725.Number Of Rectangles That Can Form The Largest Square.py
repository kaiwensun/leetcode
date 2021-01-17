iclass Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxLen = max(min(r) for r in rectangles)
        return len([r for r in rectangles if min(r) >= maxLen])

