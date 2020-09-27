class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        for i in xrange(len(timeSeries) - 1):
            res += min(duration, timeSeries[i + 1] - timeSeries[i])
        return res + duration if timeSeries else 0

