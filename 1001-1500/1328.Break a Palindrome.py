class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        l = list(palindrome)
        n = len(palindrome)
        for i in xrange(n):
            if l[i] != "a" and i * 2 != len(l) - 1:
                l[i] = "a"
                return "".join(l)
        for i in xrange(n - 1, -1, -1):
            if l[i] != "b" and i * 2 != len(l) - 1:
                l[i] = "b"
                return "".join(l)
        return ""
