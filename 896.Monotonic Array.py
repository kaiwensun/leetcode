class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        direction = 0
        for i in xrange(1, len(A)):
            if direction:
                d = cmp(A[i], A[i - 1])
                if direction != d and d != 0:
                    return False
            else:
                direction = cmp(A[i], A[i - 1])
        return True
