from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        common = cnt.most_common(3)
        if len(common) > 2:
            return False
        if len(cnt) == 2:
            return (1, 1) in common or (abs(common[0][0] - common[1][0]) == 1 and cnt[max(common[1][0], common[0][0])] == 1)
        return 1 in set(cnt.keys()) or 1 in set(cnt.values())

