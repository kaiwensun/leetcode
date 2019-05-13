class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2[:len(s1)])
        meet = 0
        for c in c1:
            if c1[c] == c2[c]:
                meet += 1
        if meet == len(c1):
            return True
        target_meet = len(c1)
        for i in xrange(len(s1), len(s2)):
            added = s2[i]
            removed = s2[i - len(s1)]
            if added == removed:
                continue
            if c1[removed] == c2[removed]:
                meet -= 1
            c2[removed] -= 1
            if c1[removed] == c2[removed] != 0:
                meet += 1
            if c1[added] == c2[added] != 0:
                meet -= 1
            c2[added] += 1
            if c1[added] == c2[added]:
                meet += 1
            if meet == target_meet:
                return True
        return False
