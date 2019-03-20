class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K >= 2:
            return ''.join(sorted(S))
        c = min(S)
        candidates = set()
        if S[0] == c:
            candidates.add(0)
        for i in xrange(1, len(S)):
            if c == S[i] != S[i - 1]:
                candidates.add(i)
        length = len(S)
        doubled = S + S
        result = 'z' * length
        for start in candidates:
            if doubled[start:start + length] < result :
                result = doubled[start:start + length]
        return result
