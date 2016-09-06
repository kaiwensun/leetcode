class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        for c in s:
            if c in table:
                table[c]+=1
            else:
                table[c]=1
        for i in xrange(len(s)):
            if table[s[i]]==1:
                return i
        return -1
