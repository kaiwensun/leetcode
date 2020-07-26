class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        ma = minutes * 6
        ha = minutes / 2.0 + (hour % 12) * 30
        return min(abs(ma - ha), 360 - abs(ma - ha))
