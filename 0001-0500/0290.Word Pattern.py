"""
Result:
  29 / 29 test cases passed.
  Status: Accepted
  Runtime: 52 ms
  Your runtime beats 7.21% of pythonsubmissions.
Date:
  5/25/2016
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p2s = dict()
        s2p = dict()
        l = str.split()
        if len(pattern)!=len(l):
            return False
        for p,s in zip(pattern,l):
            b1 = p in p2s
            b2 = s in s2p
            if b1 and b2:
                if p2s[p]==s and s2p[s]==p:
                    continue
                else:
                    return False
            elif not b1 and not b2:
                p2s[p]=s
                s2p[s]=p
            else:
                return False
        return True
