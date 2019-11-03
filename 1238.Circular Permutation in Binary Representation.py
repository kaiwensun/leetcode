class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        gray = [(b >> 1) ^ b for b in xrange(1 << n)]
        index = gray.index(start)
        return gray[index:] + gray[:index]
