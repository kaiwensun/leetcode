class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = res = 0
        vowels = "aeiou"
        for i, c in enumerate(s):
            if c in vowels:
                cnt += 1
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)
        return res
            
