"""
Basic idea:
	sort intervals by their start
	merge intervals by picking intervals one by one. if can merge, do merge; if can't merge, append the previous (merged) interval to the result list, and go on from the newly picked interval.

Your runtime beats 73.49% of python submissions.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x:x.start)
        res = []
        new_inter = intervals[0]
        for i in xrange(1,len(intervals)):
            if intervals[i].start<=new_inter.end:
                new_inter.end=max(new_inter.end,intervals[i].end)
            else:
                res.append(new_inter)
                new_inter=intervals[i]
        res.append(new_inter)
        return res

