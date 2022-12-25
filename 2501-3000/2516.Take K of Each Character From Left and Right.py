from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        def good(cnt):
            return all(cnt[c] >= k for c in 'abc')

        if k == 0:
            return 0
        cnt = Counter()
        r = 0
        for l in range(-1, -len(s) - 1, -1):
            cnt[s[l]] += 1
            if good(cnt):
                res = r - l
                break
        else:
            return -1
        for r in range(0, len(s)):
            cnt[s[r]] += 1
            while l <= 0 and good(cnt):
                res = min(res, r - l + 1)
                cnt[s[l]] -= 1
                l += 1
        return res

