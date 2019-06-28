class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = {x for x, y in zip(fronts, backs) if x == y}
        return min((set(fronts) | set(backs)) - same or [0])
