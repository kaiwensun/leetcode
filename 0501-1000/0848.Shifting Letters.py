class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        for i in xrange(len(shifts) - 1, 0, -1):
            shifts[i - 1] += shifts[i]
        s = list(S)
        for i in xrange(len(s)):
            s[i] = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
        return "".join(s)

