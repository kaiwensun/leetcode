class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1, s2 = s[0:len(s):2], s[1:len(s):2]
        c1, c2 = s1.count("0"), s2.count("0")
        return min(len(s1) - c1 + c2, len(s2) - c2 + c1)

