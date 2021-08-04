class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, N):
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res

