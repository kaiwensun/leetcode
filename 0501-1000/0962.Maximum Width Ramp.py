from bisect import bisect_left
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        decreasing = []
        decreasing_index = []
        res = 0
        for r_index, a in enumerate(A):
            l = bisect_left(decreasing, -a)
            if l < len(decreasing):
                l_index = decreasing_index[l]
                res = max(res, r_index - l_index)
            if not decreasing or -a > decreasing[-1]:
                decreasing.append(-a)
                decreasing_index.append(r_index)
        return res

