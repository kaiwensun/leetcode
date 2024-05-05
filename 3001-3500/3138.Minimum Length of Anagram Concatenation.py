from collections import Counter

class Solution:
    def minAnagramLength(self, s: str) -> int:
        suffix = Counter(s)
        prefix = Counter()
        for i, c in enumerate(s):
            prefix[c] += 1
            suffix[c] -= 1
            if suffix[c] == 0:
                return len(s)
            if len(prefix) == len(suffix) and len(set(suffix[c] / prefix[c] for c in suffix.keys())) == 1:
                return i + 1
        raise Exception("Unreachable")

