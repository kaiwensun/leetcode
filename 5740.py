class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        l = 0
        seen = {word[0]}
        for r in range(1, len(word)):
            if word[r] < word[r - 1]:
                l = r
                seen.clear()
            seen.add(word[r])
            if word[l] == 'a' and word[r] == "u" and len(seen) == 5:
                res = max(res, r - l + 1)
        return res

