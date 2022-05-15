from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.data = SortedList([[float("-inf"), float("-inf")], [float("inf"), float("inf")]])
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        while left <= right:
            i = self.data.bisect_left([left, -1])
            item = self.data[i]
            if self.data[i - 1][1] >= left:
                left = self.data[i - 1][1] + 1
            elif item[0] > right:
                self.data.add([left, right])
                self.cnt += right - left + 1
                break
            else:
                right = max(right, item[1])
                self.cnt -= item[1] - item[0] + 1
                self.data.pop(i)

    def count(self) -> int:
        return self.cnt



# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

