from collections import deque

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sm = sum(nums)
        length = len(nums)
        repeat = target // sm
        target %= sm
        if target == 0:
            return repeat * length
        nums *= 2
        window = deque()
        win_sum = 0
        res = float("inf")
        for num in nums:
            win_sum += num
            window.append(num)
            while win_sum > target:
                win_sum -= window.popleft()
            if win_sum == target:
                res = min(res, len(window))
        if res == float("inf"):
            return -1
        else:
            return repeat * length + res

