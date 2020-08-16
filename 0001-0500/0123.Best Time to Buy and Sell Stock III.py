class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        TRANS = 2
        # [[after_buy, after_sell], ...]
        budgets = [[float('-inf'), float('-inf')] for _ in xrange(TRANS + 1)]
        budgets[0][1] = 0
        for price in prices:
            for action in xrange(1, TRANS + 1):
                budgets[action][0] = max(budgets[action][0], budgets[action - 1][1] - price)
                budgets[action][1] = max(budgets[action][1], budgets[action][0] + price)
        return max(budget[1] for budget in budgets)
