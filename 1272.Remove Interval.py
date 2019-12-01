class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        def prune(interval, toBeRemoved):
            if interval[1]<=toBeRemoved[0] or toBeRemoved[1] <= interval[0]:
                return [interval]
            if toBeRemoved[0] <= interval[0]:
                if toBeRemoved[1] < interval[1]:
                    return [[toBeRemoved[1], interval[1]]]
                else:
                    return []
            else:
                if toBeRemoved[1] < interval[1]:
                    return [[interval[0], toBeRemoved[0]], [toBeRemoved[1], interval[1]]]
                else:
                    return [[interval[0], toBeRemoved[0]]]
        res = []
        for interval in intervals:
            res.extend(prune(interval, toBeRemoved))
        return res
