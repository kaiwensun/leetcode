import collections
class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        counter = collections.Counter(map(lambda posi: posi%2, chips))
        return min(counter[0], counter[1])
