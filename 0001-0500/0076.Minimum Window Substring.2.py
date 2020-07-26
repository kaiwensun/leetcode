from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ct = Counter(t)
        cs = Counter()
        met_c = 0
        l = r = 0
        shortl = 0
        shortr = len(s) + 1
        
        for r in xrange(len(s)):
            c = s[r]
            cs[c] += 1
            if c in ct and cs[c] == ct[c]:
                met_c += 1
            while met_c == len(ct):
                if shortr - shortl > r - l:
                    shortl, shortr = l, r
                if s[l] in ct and cs[s[l]] == ct[s[l]]:
                    met_c -= 1
                cs[s[l]] -= 1
                l += 1
        if shortr == len(s) + 1:
            shortr = -1
        return s[shortl:shortr + 1]
