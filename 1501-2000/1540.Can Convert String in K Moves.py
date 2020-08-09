from collections import Counter
class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        shifts_provided = { shift : k // 26 + int(shift <= k % 26) for shift in xrange(26)}
        shifts_needed = Counter((ord(t[i]) - ord(s[i])) % 26 for i in xrange(len(s)))
        print(shifts_provided)
        print(shifts_needed)
        for shift in xrange(1, 26):
            if shifts_needed[shift] > shifts_provided[shift]:
                return False
        return True
