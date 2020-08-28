class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        sorted_starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        sorted_ends = sorted((interval[1], i) for i , interval in enumerate(intervals))
        res = [None] * len(intervals)
        p = 0
        for end, index in sorted_ends:
            while p < len(intervals) and sorted_starts[p][0] < end:
                p += 1
            res[index] = -1 if p == len(intervals) else sorted_starts[p][1]
        return res

