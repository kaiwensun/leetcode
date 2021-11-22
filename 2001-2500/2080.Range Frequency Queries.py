from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.data = defaultdict(list)
        for i, num in enumerate(arr):
            self.data[num].append(i)


    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.data:
            return 0
        l = bisect_left(self.data[value], left)
        r = bisect_right(self.data[value], right)
        return r - l



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

