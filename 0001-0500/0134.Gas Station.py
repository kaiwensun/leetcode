class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        j = len(gas) - 1
        for i in xrange(len(gas)):
            tank += gas[i] - cost[i]
            while i != j and tank < 0:
                tank += gas[j] - cost[j]
                j -= 1
            if i == j:
                return (j + 1) % len(gas) if tank >= 0 else -1
