from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnt = Counter(answers)
        res = 0
        for ans, reporters in cnt.items():
            res += (reporters + ans) // (ans + 1) * (ans + 1)
        return res

