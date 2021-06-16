from functools import cache

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        M = len(mat)
        row_max = cache(lambda i:max(mat[i]) if 0 <= i < M else -1)
        l, r = 0, M
        while l < r:
            mid = (l + r) // 2
            if row_max(mid - 1) > row_max(mid):
                r = mid
            elif row_max(mid) < row_max(mid + 1):
                l = mid + 1
            else:
                l = r = mid
        j = mat[l].index(row_max(l))
        return l, j

