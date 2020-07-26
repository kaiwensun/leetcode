class Solution(object):
    def customSortString(self, S, T):
        cnt = collections.Counter(T)
        res = ''.join(c * cnt[c] for c in S)
        cnt -= collections.Counter(res)
        return res + ''.join(c * v for c, v in cnt.items())
