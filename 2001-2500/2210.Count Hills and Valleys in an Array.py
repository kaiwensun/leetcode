class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(-1)
        arr = []
        for i in range(N):
            if nums[i] != nums[i - 1]:
                arr.append(nums[i])
        res = 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1] or arr[i - 1] > arr[i] < arr[i + 1]:
                res += 1
        return res

