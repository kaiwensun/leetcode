import heapq

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        common = heapq.nlargest(1, ((cnt, -num) for num, cnt in Counter(num for num in nums if not num % 2).items()))
        return -common[0][1] if common else -1

