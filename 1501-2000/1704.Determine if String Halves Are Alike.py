from collections import Counter
class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt1 = Counter(s[:len(s) // 2].lower())
        cnt2 = Counter(s[len(s) // 2:].lower())
        return sum(map(lambda c: cnt1[c], "aeiou")) == sum(map(lambda c: cnt2[c], "aeiou"))

