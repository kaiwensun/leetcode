class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, last = {None: 0}, {None: 0}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i
        return max(last[c] - first[c] - 1 for c in first)

