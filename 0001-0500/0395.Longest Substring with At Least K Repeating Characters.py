from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def divideAndCounquer(start, end):
            cnt = Counter(s[start : end])
            remove = {c for c, n in cnt.iteritems() if n < k}
            if not remove:
                return end - start
            res = l = 0
            for r in xrange(start, end):
                if s[r] in remove:
                    if r != l:
                        res = max(res, divideAndCounquer(l, r))
                    l = r + 1
            if l != end:
                res = max(res, divideAndCounquer(l, end))
            return res
        return divideAndCounquer(0, len(s))

