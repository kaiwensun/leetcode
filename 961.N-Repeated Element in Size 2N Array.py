class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = set()
        for a in A:
            if a in s:
                return a
            s.add(a)
