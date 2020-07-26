class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        cnt = collections.Counter(hand)
        keys = sorted(cnt.keys())
        for key in keys:
            if cnt[key] < 0:
                return False
            if cnt[key] == 0:
                continue
            mn = min(cnt[k] for k in xrange(key, key + W))
            if mn != cnt[key]:
                return False
            for k in xrange(key, key + W):
                cnt[k] -= mn
        return True
