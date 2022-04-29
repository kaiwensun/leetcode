class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        def in_circles(i, j):
            for x, y, r in circles:
                if (i - x) **2 + (j - y) ** 2 <= r ** 2:
                    return True
            return False
        mxx, mxy = float("-inf"), float("-inf")
        mnx, mny = float("inf"), float("inf")
        for x, y, r in circles:
            mxx = max(mxx, x + r)
            mxy = max(mxy, y + r)
            mnx = min(mnx, x - r)
            mny = min(mny, y - r)
        res = 0
        for i in range(mnx, mxx + 1):
            for j in range(mny, mxy + 1):
                if in_circles(i, j):
                    res += 1
        return res

