class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        mx = max(a, b, c)
        mn = min(a, b, c)
        md = [k for k in a, b, c if k not in (mx, mn)][0]
        rmax = mx - mn - 2
        m = [mx - md, md - mn]
        if m == [1, 1]:
            rmin = 0
        elif 2 in m or 1 in m:
            rmin = 1
        else:
            rmin = 2
        return [rmin, rmax]
