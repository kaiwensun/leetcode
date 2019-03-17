class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1
        i = len(A) - 1
        while i >= 0 and (even <=i or odd <= i):
            if i % 2 == A[i] % 2:
                i -= 1
            else:
                if A[i] % 2 == 1:
                    A[i], A[odd] = A[odd], A[i]
                    odd += 2
                else:
                    A[i], A[even] = A[even], A[i]
                    even += 2
        return A
