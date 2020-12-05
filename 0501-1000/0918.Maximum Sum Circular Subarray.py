class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # subarray that does not cycle
        l = r = 0
        res = float("-inf")
        sm = 0
        for r in xrange(len(A)):
            sm += A[r]
            res = max(res, sm)
            if sm <= 0:
                l = r + 1
                sm = 0
        # subarray that does cycle
        from_left = [A[0]] * len(A)
        sm = A[0]
        for i in xrange(1, len(A)):
            sm += A[i]
            from_left[i] = max(from_left[i - 1], sm)
        sm = A[-1]
        from_right = [A[-1]] * len(A)
        for i in xrange(len(A) - 2, -1, -1):
            sm += A[i]
            from_right[i] = max(from_right[i + 1], sm)
        for i in xrange(1, len(A)):
            res = max(res, from_left[i - 1] + from_right[i])
        return res

