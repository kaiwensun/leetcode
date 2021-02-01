class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        for primary in set(s):
            diff = l = r = 0
            while r < len(s):
                r += 1
                if s[r - 1] != primary:
                    diff += 1
                    if diff > k:
                        while s[l] == primary:
                            l += 1
                        l += 1
                        diff -= 1
                res = max(res, r - l)
        return res

