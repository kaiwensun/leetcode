from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(num)
        return all(cnt[str(i)] == int(num[i]) for i in range(len(num)))

