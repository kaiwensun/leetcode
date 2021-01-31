import bisect
class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        for i in xrange(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]
        answer = []
        for favoriteType, favoriteDay, dailyCap in queries:
            mx = dailyCap * (favoriteDay + 1)
            r = bisect.bisect_left(candiesCount, mx)
            l = bisect.bisect_left(candiesCount, favoriteDay + 1)
            answer.append(l <= favoriteType <= r)
        return answer

