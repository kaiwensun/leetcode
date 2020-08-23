class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        return sum(piles[i] for i in xrange(1, len(piles) / 3 * 2, 2))

