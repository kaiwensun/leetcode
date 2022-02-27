from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        diff1, diff2 = c1 - c2, c2 - c1
        return sum(diff1.values()) + sum(diff2.values())

