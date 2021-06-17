class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        def test(k, width):
            delta, sm = 1, 0
            for _ in xrange(width + 1):
                sm += delta
                delta *= k
            return sm

        n = int(n)
        max_width = int(math.log(n, 2))
        for width in xrange(max_width, 0, -1):
            k = int(math.pow(n, 1.0 / width))
            if k > 1 and test(k, width) == n:
                return str(k)
        return str(n - 1)

