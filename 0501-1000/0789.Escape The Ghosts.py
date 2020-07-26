class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        distance = sum(map(abs, target))
        for ghost in ghosts:
            d = sum(map(abs, (target[0] - ghost[0], target[1] - ghost[1])))
            if d <= distance:
                return False
        return True
