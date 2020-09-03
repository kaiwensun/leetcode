class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for size in xrange(1, len(s)):
            if len(s) % size == 0:
                if s[:size] * (len(s) // size) == s:
                    return True
        return False

