class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        mn = float('inf')
        for i in xrange(len(A) - 1, -1, -1):
            if mn < A[i]:
                mx = float('-inf')
                mx_ind = None
                for j in xrange(i + 1, len(A)):
                    if mx < A[j] < A[i]:  # A testcase was wrong during the contest. fixed now.
                        mx_ind = j
                        mx = A[j]
                A[i], A[mx_ind] = A[mx_ind], A[i]
                return A
            else:
                mn = min(mn, A[i])
        return A
