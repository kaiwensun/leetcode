from collections import Counter
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        drifts = []
        for a, b in zip(A, B):
            if a != b:
                drifts.append((a, b))
            if len(drifts) > 2:
                return False
        return (len(drifts) == 2 and drifts[0] == tuple(reversed(drifts[1]))) \
            or (A and len(drifts) == 0 and Counter(A).most_common(1)[0][1] > 1)

