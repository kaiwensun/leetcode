class Solution(object):
    def numWaterBottles(self, full, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = 0
        empty = 0
        while full:
            res += full
            empty += full
            full = empty / numExchange
            empty -= full * numExchange
        return res
