class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        exists = collections.defaultdict(collections.Counter)
        for i, front in enumerate(fronts):
            exists[front][i] += 1
        for i, back in enumerate(backs):
            exists[back][i] += 1
        for num in sorted(set(fronts) | set(backs)):
            if all(map(lambda cnt: cnt <= 1, exists[num].values())):
                return num
        return 0
