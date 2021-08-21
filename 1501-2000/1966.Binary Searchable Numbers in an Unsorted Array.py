class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        mn, mx = float("inf"), float("-inf")
        left, right = set(), set()
        for num in nums:
            mx = max(mx, num)
            if mx <= num:
                left.add(num)
        for num in reversed(nums):
            mn = min(mn, num)
            if num <= mn:
                right.add(num)
        return len(left & right)

