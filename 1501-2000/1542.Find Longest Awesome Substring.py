class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {0: -1}
        prefix = 0
        res = 1
        for i, d in enumerate(s):
            prefix ^= (1 << int(d))
            if prefix in seen:
                res = max(res, i - seen[prefix])
            for shift in xrange(10):
                wanted = prefix ^ 1 << shift
                if wanted in seen:
                    res = max(res, i - seen[wanted])
            seen.setdefault(prefix, i)
        return res
