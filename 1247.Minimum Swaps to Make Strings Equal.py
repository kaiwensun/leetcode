class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        cnt = [0, 0]
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                cnt[s1[i] == 'x'] += 1
        if sum(cnt) % 2 != 0:
            return -1
        return sum((cnt[i] / 2 + cnt[i] % 2) for i in xrange(2))
