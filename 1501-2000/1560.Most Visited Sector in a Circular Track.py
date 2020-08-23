class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        if rounds[0] == rounds[-1]:
            return [rounds[0]]
        if rounds[0] < rounds[-1]:
            return range(rounds[0], rounds[-1] + 1)
        return range(1, rounds[-1] + 1) + range(rounds[0], n + 1)
