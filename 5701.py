class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff = [pair for pair in zip(s1, s2) if pair[0] != pair[1]]
        if diff:
            return len(diff) == 2 and diff[0] == tuple(reversed(diff[1]))
        return True

