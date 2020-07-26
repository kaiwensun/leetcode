class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num in [1<<(2*i) for i in range(16)]:
            return True
        return False;
        
