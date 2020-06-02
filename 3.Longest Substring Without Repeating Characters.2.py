import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = collections.Counter()
        res = l = 0
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] == 2:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
