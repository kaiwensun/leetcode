class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        profit, res, rotate = 0, 0, -1
        remain = 0
        i = 0
        while i < len(customers) or remain != 0:
            if i < len(customers):
                remain += customers[i]
            onboard = min(4, remain)
            remain -= onboard
            profit = profit + onboard * boardingCost - runningCost
            i += 1
            if profit > res:
                res = profit
                rotate = i
        return rotate

