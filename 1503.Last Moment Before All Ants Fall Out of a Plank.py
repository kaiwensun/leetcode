class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        l = max(left or [0])
        r = min(right or [n])
        return max([n - r, l])
