from sortedcontainers import SortedList

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        indexes = SortedList(range(len(nums)))
        res = cur = i = 0
        for num, index in sorted([num, index] for index, num in enumerate(nums)):
            cur = i % len(indexes)
            i = indexes.index(index)
            res += (i - cur) % len(indexes)
            indexes.pop(i)
        return res + len(nums)

