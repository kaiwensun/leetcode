class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return Counter(zip(s[:-1], s[1:]))[tuple("01")] < 1

