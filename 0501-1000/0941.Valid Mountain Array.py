class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increasing = None
        i = 0
        while i + 1 < len(A):
            if A[i] == A[i + 1]:
                return False
            if A[i] > A[i + 1]:
                if increasing is None:
                    return False
                break
            increasing = True
            i += 1
        else:
            return False
        increasing = False
        while i + 1 < len(A):
            if A[i] == A[i + 1]:
                return False
            if A[i] < A[i + 1]:
                return False
            i += 1
        return True

