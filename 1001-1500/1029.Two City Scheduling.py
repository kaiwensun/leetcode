class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff = [(cost[0] - cost[1], cost) for cost in costs]
        diff.sort()
        N = len(costs) / 2
        return sum(pair[1][0] for pair in diff[:N]) + sum(pair[1][1] for pair in diff[N:])
