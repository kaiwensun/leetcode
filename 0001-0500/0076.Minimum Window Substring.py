#Result:
# 266 / 266 test cases passed.
# Status: Accepted
# Runtime: 172 ms
# Your runtime beats 63.75% of python submissions.
#Date:
# 10/2/2016

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic_t = {}
        for c in t:
            if c in dic_t:
                dic_t[c]+=1
            else:
                dic_t[c]=1
        dic_s = dict(zip(t,[0]*len(t)))
        incdLtr = 0;    #count of included letters
        rtn = s+'#'     #lenth add one to decide whether rtn has been modified
        l,r = 0,0
        
        while r<len(s):
            while incdLtr!=len(t) and r<len(s):
                if s[r] in dic_t:
                    dic_s[s[r]]+=1
                    if dic_s[s[r]]<=dic_t[s[r]]:
                        incdLtr+=1
                r+=1
            if incdLtr<len(t):
                break
            while s[l] not in dic_s or dic_s[s[l]]>dic_t[s[l]]:
                if s[l] in dic_s:
                    dic_s[s[l]]-=1
                l+=1
            else:
                substr = s[l:r]
                if len(rtn)>len(substr):
                    rtn = substr
                dic_s[s[l]]-=1
                l+=1
                incdLtr-=1
        return rtn if len(rtn)<=len(s) else ''
