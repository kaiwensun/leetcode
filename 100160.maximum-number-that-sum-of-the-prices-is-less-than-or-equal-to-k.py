class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def test(num):
            pulse = 1 << x - 1
            res = 0
            while pulse <= num:
                mask = (pulse << 1) - 1
                right = num & mask
                left = num - right
                res += (left >> 1) + max(0, right - pulse + 1)
                pulse <<= x
            return res <= k

        l, r = 1, 10 ** 18 + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

