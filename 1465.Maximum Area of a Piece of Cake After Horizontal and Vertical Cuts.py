class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        mx_w = mx_h = 0
        prev_w = prev_h = 0
        horizontalCuts.sort()
        verticalCuts.sort()
        for cut in verticalCuts:
            mx_w = max(mx_w, cut - prev_w)
            prev_w = cut
        mx_w = max(mx_w, w - prev_w)
        for cut in horizontalCuts:
            mx_h = max(mx_h, cut - prev_h)
            prev_h = cut
        mx_h = max(mx_h, h - prev_h)
        return (mx_h * mx_w) % (10 ** 9 + 7)
        
