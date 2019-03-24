class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        s /= 3
        targets = [2 * s, s]
        acc = 0
        for a in A:
            acc += a
            if acc == targets[-1]:
                targets.pop()
            if not targets:
                return True
        return False
