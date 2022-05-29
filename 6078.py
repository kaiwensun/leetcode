from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tc = Counter(target)
        sc = Counter(s)
        return min(sc[c] // tc[c] for c in tc.keys())

