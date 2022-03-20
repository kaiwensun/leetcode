from sortedcontainers import SortedList

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        bst = SortedList([0])
        res = sm = 0
        for num in nums:
            sm += num
            ind1 = bst.bisect_left(sm - upper)
            ind2 = bst.bisect_right(sm - lower)
            res += ind2 - ind1
            bst.add(sm)
        return res


