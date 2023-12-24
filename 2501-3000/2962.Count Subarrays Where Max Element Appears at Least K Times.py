class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        mx = max(nums)
        indexes = [i for i, num in enumerate(nums) if num == mx]
        if len(indexes) < k:
            return 0
        l, r = 0, k - 1
        n = len(nums)
        indexes.append(n)
        while r < len(indexes) - 1:
            res += (indexes[l] + 1) * (indexes[r + 1] - indexes[r])
            l += 1
            r += 1
        return res

