class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums) | {0}
        return -1 if (res := max(num for num in s if num >= 0 and -num in s)) == 0 else res

