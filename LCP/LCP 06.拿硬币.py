class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        return sum(coin // 2 + coin % 2 for coin in coins)

