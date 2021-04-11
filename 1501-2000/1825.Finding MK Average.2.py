from collections import deque
from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        
        self.ksmallest = SortedList()
        self.middle = SortedList()
        self.klargest = SortedList()
        self.sum = 0
        
    def addElement(self, num: int) -> None:
        if len(self.queue) == self.m:
            expired = self.queue.popleft()
            if expired <= self.ksmallest[-1]:
                self.ksmallest.remove(expired)
            elif self.middle and expired <= self.middle[-1]:
                self.sum -= expired
                self.middle.remove(expired)
            else:
                self.klargest.remove(expired)
        self.queue.append(num)
        self.middle.add(num)
        self.sum += num
        if self.ksmallest:
            self.sum += self.ksmallest[-1]
            self.middle.add(self.ksmallest.pop(-1))
        if self.klargest:
            self.sum += self.klargest[0]
            self.middle.add(self.klargest.pop(0))
        while self.middle and len(self.ksmallest) < self.k:
            self.sum -= self.middle[0]
            self.ksmallest.add(self.middle.pop(0))
        while self.middle and len(self.klargest) < self.k:
            self.sum -= self.middle[-1]
            self.klargest.add(self.middle.pop())


    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1
        return self.sum // (self.m - self.k * 2)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

