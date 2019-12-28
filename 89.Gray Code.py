class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cur = [0]
        for i in xrange(n):
            cur = cur + [(1 << i) | ele for ele in reversed(cur)]
        return cur
