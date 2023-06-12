class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        for i in xrange(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]
        candiesCount.append(0)
        return [favoriteDay + 1 <= candiesCount[favoriteType] and candiesCount[favoriteType - 1] < dailyCap * (favoriteDay + 1) for favoriteType, favoriteDay, dailyCap in queries]

