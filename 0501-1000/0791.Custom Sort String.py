class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        d = {c:i for i, c in enumerate(S)}
        return ''.join(sorted(T, key=lambda c: d.get(c, -1)))
