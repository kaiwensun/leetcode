class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        cnt = 0
        cover = [-1, -1]
        for interval in sorted(intervals):
            if not cover[0] == interval[0] and not cover[1] >= interval[1]:
                cnt += 1
            if interval[1] > cover[1]:
                cover = interval    
        return cnt
