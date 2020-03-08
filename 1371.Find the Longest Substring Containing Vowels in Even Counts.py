class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = 'aeiou'
        left = {0: -1}
        res = mask = 0
        for i, c in enumerate(s):
            shift = vowels.find(c)
            if shift >= 0:
                mask ^= 1 << shift
            left.setdefault(mask, i)
            res = max(res, i - left[mask])
        return res
