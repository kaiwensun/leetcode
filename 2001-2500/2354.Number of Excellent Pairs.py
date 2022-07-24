class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        bits = sorted(bin(num).count('1') for num in nums)
        res = 0
        N = len(bits)
        r = N - 1
        for l in range(N):
            while r >= 0 and bits[l] + bits[r] >= k:
                r -= 1
            res += N - 1 - r
        return res

