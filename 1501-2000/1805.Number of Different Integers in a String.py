class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        res = [""]
        for c in word:
            if c.isdigit():
                res[-1] += c
            elif res[-1]:
                res.append("")
        s = set(int(num) for num in res if num)
        return len(s)

