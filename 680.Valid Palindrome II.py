class Solution(object):
    def validPalindrome(self, s, life=1):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange((len(s) + 1)/ 2):
            if s[i] != s[-i - 1]:
                if life:
                    return self.validPalindrome(s[i:len(s) - i - 1], 0) or self.validPalindrome(s[i + 1:len(s) - i], 0)
                else:
                    return False
        return True
