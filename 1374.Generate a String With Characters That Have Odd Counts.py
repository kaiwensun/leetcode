class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2:
            return 'a' * n
        else:
            return 'a' + 'b' * (n - 1)
