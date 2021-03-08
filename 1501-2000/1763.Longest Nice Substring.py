from collections import defaultdict, Counter
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def divide_and_conquer(start, end):
            cnt = Counter()
            for i in xrange(start, end):
                cnt[s[i]] += 1
            res = -1, -1
            invalid = {c for c in cnt.keys() if get_buddy(c) not in cnt}
            if not invalid:
                return start, end
            pre = start
            for i in xrange(start, end + 1):
                if i == end or s[i] in invalid:
                    subres = divide_and_conquer(pre, i)
                    if subres[1] - subres[0] > res[1] - res[0]:
                        res = subres
                    pre = i + 1
            return res

        def get_buddy(c):
            return c.lower() if "A" <= c <= "Z" else c.upper()

        start, end = divide_and_conquer(0, len(s))
        return s[start: end]

