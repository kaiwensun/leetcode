class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for shift in range(30):
            cnt = 0
            for num in nums:
                cnt += (num >> shift) & 1
            res += cnt * (len(nums) - cnt)
        return res
