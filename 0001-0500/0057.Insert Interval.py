"""
The idea is in three steps:

insert newInterval to intervals based on Interval.start using binary search bisect.bisect_left
merge with intervals right to the inserted newInterval
merge with intervals left to the inserted newInterval
If I can assume the number of intervals overlapping with newInterval is bounded by a constant c, then the complexity of this algorithm is O(log n + c) = O(log n).

Even if it is not bounded, we still have c≤n, and O(log n + n)=O(n).

But why is it so slow and beats only 15% of Python submission?

"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from bisect import bisect_left

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        #insert newInterval to intervals according to .start. binary search takes O(log n)
        Interval.__cmp__=lambda inter1,inter2:inter1.start-inter2.start
        index = bisect_left(intervals,newInterval)
        intervals.insert(index,newInterval)

        #merge with intervals right to newInterval
        i=index+1
        while i<len(intervals):
            if newInterval.end<intervals[i].start:
                break
            if newInterval.end>=intervals[i].start and newInterval.end<=intervals[i].end:
                intervals[index].end=intervals[i].end
                del intervals[i]
            else:
                del intervals[i]

        #merge with the only one interval (if there is one) fully covers newInterval
        if index>0:
            if intervals[index-1].end>newInterval.end:
                intervals[index].end=intervals[index-1].end
        i=index-1

        #merge with intervals left to newInterval
        while i>=0:
            if intervals[i].end<newInterval.start:
                break
            else:
                intervals[i+1].start = intervals[i].start
                del intervals[i]
                i-=1
        return intervals

