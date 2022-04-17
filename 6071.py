from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        res = 0
        for value in Counter(tasks).values():
            if value == 1:
                return -1
            res += (value - 1) // 3 + 1
        return res

