class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        offer = A[0]
        rval = float('-inf')
        for i in xrange(1, len(A)):
            rval = max(rval, offer + A[i] - i)
            offer = max(offer, A[i] + i)
        return rval
