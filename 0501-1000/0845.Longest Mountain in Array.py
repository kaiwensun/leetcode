class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def get_left(i):
            return float("inf") if i == 0 else A[i - 1]
        
        def get_right(i):
            return float("inf") if i == len(A) - 1 else A[i + 1]
        
        def is_start(i):
            return get_left(i) >= A[i] < get_right(i)
        
        def is_end(i):
            return get_left(i) > A[i] <= get_right(i)
        
        def is_peak(i):
            return get_left(i) < A[i] > get_right(i)
        res = 0
        seen_peak = False
        for i in xrange(len(A)):
            if is_end(i) and seen_peak:
                seen_peak = False
                res = max(res, i - start + 1)
            if is_start(i):
                start = i
            if is_peak(i):
                seen_peak = True
        return res

