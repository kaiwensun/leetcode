class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 == 1:
            return (n + 1) // 2 * (n // 2)
        else:
            return n * n // 4
