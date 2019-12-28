class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(n):
            res += [(1 << i) | ele for ele in reversed(res)]
        shift = random.randint(0, n)
        return [((ele << shift) & ((1 << n) - 1)) | (ele >> (n - shift)) for ele in res]
