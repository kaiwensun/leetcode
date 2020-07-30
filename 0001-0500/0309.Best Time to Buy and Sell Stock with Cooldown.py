class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, empty, hold = float('-inf'), 0, 0, float('-inf')
        for price in prices:
            new_buy = empty - price
            new_sell = max(hold + price, buy + price)
            new_empty = max(empty, sell)
            new_hold = max(buy, hold)
            buy, sell, empty, hold = new_buy, new_sell, new_empty, new_hold
        return max(sell, empty)
