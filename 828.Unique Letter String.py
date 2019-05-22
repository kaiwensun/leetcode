class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        seen_at = collections.defaultdict(list)
        res = 0
        mod = 10 ** 9 + 7
        for i, c in enumerate(S):
            seen_at[c].append(i)
        for c, lst in seen_at.items():
            for i in xrange(len(lst)):
                pre = -1 if i == 0 else lst[i - 1]
                this = lst[i]
                nxt = len(S) if i == len(lst) - 1 else lst[i + 1]
                res += (this - pre) * (nxt - this)
                res %= mod
        return res
