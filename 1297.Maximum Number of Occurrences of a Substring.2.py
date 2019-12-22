import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter(filter(lambda w: len(set(w)) <= maxLetters, (s[i:i + minSize] for i in range(len(s) - minSize + 1)))).most_common(1)
        return res[0][1] if res else 0
