#Basic idea:
# from every char of the string, take it as the center and try to expand palindromic substring
#Result:
# 88 / 88 test cases passed.
# Status: Accepted
# Runtime: 1266 ms
# Your runtime beats 23.86% of python submissions.
#Date:
# 9/21/2016

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rtn = (0,0)
        for center in xrange(len(s)):
            rtn = self.getLongest(rtn,self.extend(s,center,center))
            rtn = self.getLongest(rtn,self.extend(s,center,center+1))
        return s[rtn[0]:rtn[0]+rtn[1]]
        
    def extend(self,s,l,r):
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
        return (l+1,r-l-1)
    
    def getLongest(self,tup1,tup2):
        return tup1 if tup1[1]>tup2[1] else tup2
