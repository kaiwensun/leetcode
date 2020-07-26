class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        length = self.calcLen(S)
        return self.decodeAtIndexWithLen(S, K, length, len(length))
        

    def decodeAtIndexWithLen(self, S, K, length, end):
        index = bisect.bisect_left(length, K, hi=end)
        new_K = K % length[index - 1]
        if length[index] == K or new_K == 0:
            return self.lookLeftForLetter(S, index)
        return self.decodeAtIndexWithLen(S, new_K, length, end=index)
        
        
    def calcLen(self, S):
        rval = [1] * len(S)
        for i in xrange(1, len(S)):
            if S[i].islower():
                rval[i] = rval[i - 1] + 1
            else:
                rval[i] = rval[i - 1] * int(S[i])
        return rval
    
    def lookLeftForLetter(self, S, end):
        while S[end].isdigit():
            end -= 1
        return S[end]
