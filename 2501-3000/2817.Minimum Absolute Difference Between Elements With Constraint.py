from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        lst = SortedList()
        res = float("inf")
        for i in range(len(nums) - x):
            lst.add(nums[i])
            num1 = nums[i + x]
            num2_index = lst.bisect_left(num1)
            for j in [num2_index - 1, num2_index]:
                if 0 <= j < len(lst):
                    res = min(res, abs(num1 - lst[j]))
        return res

