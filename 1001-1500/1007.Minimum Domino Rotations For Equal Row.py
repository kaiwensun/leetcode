class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        candidates = list(set([A[0], B[0]]))
        for i in xrange(len(A)):
            for candidate in candidates:
                if candidate != A[i] and candidate != B[i]:
                    candidates.remove(candidate)
            if not candidates:
                return -1
        rval = len(A)
        for candidate in candidates:
            a_cnt = len([x for x in A if x != candidate])
            b_cnt = len([x for x in B if x != candidate])
            rval = min(rval, a_cnt, b_cnt)
        return rval
