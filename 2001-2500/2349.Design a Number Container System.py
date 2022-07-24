import heapq, collections

class NumberContainers:

    def __init__(self):
        self.index2num = {}
        self.num2indexes = collections.defaultdict(list)


    def change(self, index: int, number: int) -> None:
        self.index2num[index] = number
        heapq.heappush(self.num2indexes[number], index)


    def find(self, number: int) -> int:
        while self.num2indexes[number] and self.index2num[self.num2indexes[number][0]] != number:
            heapq.heappop(self.num2indexes[number])
        return self.num2indexes[number][0] if self.num2indexes[number] else -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

