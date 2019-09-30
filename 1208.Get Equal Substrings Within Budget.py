class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        def diff(i):
            return abs(ord(s[i]) - ord(t[i]))

        l = r = acc = res = 0
        while r < len(s):
            acc += diff(r)
            r += 1
            while acc > maxCost:
                acc -= diff(l)
                l += 1
            res = max(res, r - l)
        return res
