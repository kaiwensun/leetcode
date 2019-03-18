class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        leading_one = self.getLeadingOne(N)
        mask = (leading_one << 1) - 1
        return (~N) & mask
    
    def getLeadingOne(self, n):
        return 1 << int(math.log(n, 2))
