"""
Basic idea:
	use dynamic programming, dp[i][j] means if the first i char(s) of s and first j char(s) of p match
	use preprocess to simplify pattern p, and pre-determine some simple impossible cases
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = list(p)
        s = list(s)
        prejudge = self.preprocess(p,s)
        if prejudge==False:
            return False
        dp=[[False]*(len(p)+1) for x in xrange(len(s)+1)]
        dp[0][0]=True
        try:
            if p[0]=='*':
                for i in xrange(len(s)+1):
                    dp[i][1]=True
        except:
            pass
        for pindex in xrange(len(p)):
            if pindex==0 and p[0]=='*':
                continue
            hopeful = False
            for sindex in xrange(len(s)):
                if s[sindex]==p[pindex] or p[pindex]=='?':
                    if dp[sindex][pindex]==True:
                        dp[sindex+1][pindex+1]=True
                        hopeful=True
                    else:
                        pass
                elif p[pindex]=='*':
                    if dp[sindex+1][pindex]:# or dp[sindex+1][pindex]:
                        for i in xrange(sindex,len(s)):
                            dp[i+1][pindex+1]=True
                        hopeful=True
                        break
            if hopeful==False:
                return False
        return dp[len(s)][len(p)]
    
    def preprocess(self,p,s):
        i = 0
        while i<len(p)-1:
            if p[i]==p[i+1] and p[i]=='*':
                del p[i]
            elif p[i]=='*' and p[i+1]=='?':
                p[i]='?'
                p[i+1]='*'
                i=i+1
            else:
                i=i+1
        while min(len(p),len(s))>0:
            if p[-1]==s[-1] or p[-1]=='?':
                del p[-1]
                del s[-1]
            elif p[-1]!='*':
                return False
            else:
                break
        countstar=reduce(lambda x,y:x+(1 if y=='*' else 0),p,0)
        if len(p)-countstar>len(s):
            return False
        return True

"""
Here is another solution by youke
https://leetcode.com/discuss/38645/128ms-o-1-space-python-solution
"""

class Solution2:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p:
            return not s

        m, n = len(s), len(p)
        i = j = 0
        last_x = 0
        last_y = -1
        while i < m:
            if j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                last_x = i
                last_y = j
                j += 1
            elif last_y >= 0:
                i = last_x + 1
                last_x += 1
                j = last_y
            else:
                return False

        while j < n and p[j] == '*':
            j += 1

        return j == n

