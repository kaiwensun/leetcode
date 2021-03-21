class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        def is_valid(num):
            left = min(num - 1, index)
            right = min(num - 1, n - index - 1)
            sm = (num - 1 + num - left) * left // 2 + (num - 1 + num - right) * right // 2 + num
            return sm <= maxSum
        l, r = 1, 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if is_valid(mid):
                l = mid + 1
            else:
                r = mid
        return l

