class Solution(object):
    def lastRemaining(self, n, is_l2r=True):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if is_l2r:
            return self.lastRemaining(n // 2, not is_l2r) * 2
        else:
            if n % 2 == 0:
                return self.lastRemaining(n // 2, not is_l2r) * 2 - 1
            else:
                return self.lastRemaining(n // 2, not is_l2r) * 2
