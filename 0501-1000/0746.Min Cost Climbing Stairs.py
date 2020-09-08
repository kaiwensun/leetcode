class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        return min(reduce(lambda (c1, c2), c: (c2, c + min(c1, c2)), cost, (0, 0)))

