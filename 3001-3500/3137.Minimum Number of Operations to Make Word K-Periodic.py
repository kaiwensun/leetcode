from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = Counter()
        for i in range(0, len(word), k):
            cnt[word[i:i+k]] += 1
        return len(word) // k - max(cnt.values())

