class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        N = len(S)
        res = [float('inf')] * N
        dist = float('inf')
        for i in xrange(N):
            dist = 0 if S[i] == C else dist + 1
            res[i] = min(res[i], dist)
        dist = float('inf')
        for i in xrange(N -1, -1, -1):
            dist = 0 if S[i] == C else dist + 1
            res[i] = min(res[i], dist)
        return res
