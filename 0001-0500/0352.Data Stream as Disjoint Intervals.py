from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, val: int) -> None:
        index = self.intervals.bisect_right([val, float("inf")])
        if index < len(self.intervals) and self.intervals[index][0] == val + 1:
            self.intervals[index][0] = val
        else:
            self.intervals.add([val, val])
        if index != 0 and self.intervals[index - 1][1] >= val - 1:
            self.intervals[index][0] = self.intervals[index - 1][0]
            self.intervals[index][1] = max(self.intervals[index - 1][1], self.intervals[index][1])
            self.intervals.pop(index - 1)

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals)



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

