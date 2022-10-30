from statistics import mean

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr = [num for num in nums if num % 6 == 0]
        return int(mean(arr)) if arr else 0

