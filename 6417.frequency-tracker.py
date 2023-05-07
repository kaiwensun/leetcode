from collections import Counter, defaultdict

class FrequencyTracker:

    def __init__(self):
        self.cnt = Counter()
        self.freq = defaultdict(set)

    def add(self, number: int) -> None:
        self.freq[self.cnt[number]] -= {number}
        self.cnt[number] += 1
        self.freq[self.cnt[number]].add(number)

    def deleteOne(self, number: int) -> None:
        if self.cnt[number] > 0:
            self.freq[self.cnt[number]].remove(number)
            self.cnt[number] -= 1
            if self.cnt[number]:
                self.freq[self.cnt[number]].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return bool(self.freq.get(frequency))


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

