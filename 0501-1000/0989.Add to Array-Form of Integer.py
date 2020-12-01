class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        carry = K
        for i in xrange(len(A) - 1, -1, -1):
            res = A[i] + carry
            carry = res // 10
            A[i] = res % 10
        while carry:
            A.insert(0, carry % 10)
            carry //= 10
        return A

