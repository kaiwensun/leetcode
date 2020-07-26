class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = max(arr)
        if res <= 0:
            return res
        res = float('-inf')
        minimum = float('inf')
        s_full = 0
        s_1out = float('-inf')
        for n in arr:
            minimum = min(minimum, n)
            s_full += n
            s_1out += n
            if minimum < 0:
                s_1out = max(s_1out, s_full - minimum)
                res = max(res, s_1out)
            else:
                res = max(res, s_full, s_1out)
            if s_full < 0 and minimum <=0:
                s_full = 0
                minimum = float('inf')
            if s_1out <= 0:
                s_1out = float('-inf')
        return res
