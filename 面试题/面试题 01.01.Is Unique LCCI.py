class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        mask = 0
        for c in astr:
            bit = 1 << (ord(c) - ord('a'))
            if bit & mask:
                return False
            mask |= bit
        return True

