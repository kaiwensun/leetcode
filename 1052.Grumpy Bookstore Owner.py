class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        unsatisfied, mx, window = 0, 0, 0
        for i in xrange(len(grumpy)):
            unsatisfied += grumpy[i] * customers[i]
            window += grumpy[i] * customers[i]
            if i >= X:
                window -= grumpy[i - X] * customers[i - X]
            mx = max(mx, window)
        return sum(customers) - unsatisfied + mx
