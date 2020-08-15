class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = 0
        right = float("-inf")
        for a, b in sorted(intervals):
            if a < right:
                res += 1
                right = min(right, b)
            else:
                right = b
        return res

