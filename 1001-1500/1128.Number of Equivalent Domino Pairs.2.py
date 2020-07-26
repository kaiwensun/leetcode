class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter(map(tuple, map(sorted, dominoes)))
        print counter
        return sum(x * (x - 1) / 2 for x in counter.values())
