import collections
CROAK="croak"
class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        min_frogs = cur_frogs = 0
        cnt = collections.Counter()
        prev = dict(zip(CROAK[1:], CROAK))
        for sound in croakOfFrogs:
            cnt[sound] += 1
            cnt[prev.get(sound)] -= 1
            if prev.get(sound) and cnt[prev[sound]] < 0:
                return -1
            if sound == CROAK[0]:
                cur_frogs += 1
            elif sound == CROAK[-1]:
                cur_frogs -= 1
            min_frogs = max(min_frogs, cur_frogs)
        cnt[CROAK[-1]] = cnt[None] = 0
        return -1 if sum(cnt.values()) else min_frogs
