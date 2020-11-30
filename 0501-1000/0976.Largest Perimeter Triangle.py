class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = b = c = float("-inf")
        res = 0
        for d in sorted(A):
            a, b, c = b, c, d
            if a + b > c:
                res = a + b + c
        return res

