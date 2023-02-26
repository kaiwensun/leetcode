class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        l, r = 0, N // 2 + 1
        while l < r:
            mid = (l + r) // 2
            if all(nums[i] * 2 <= nums[N - mid + i] for i in range(mid)):
                l = mid + 1
            else:
                r = mid
        return (l - 1) * 2

