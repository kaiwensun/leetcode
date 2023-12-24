MOD = 10 ** 9 + 7

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        right_most = {}
        for i, num in enumerate(nums):
            right_most[num] = i
        group_cnt = 0
        mx = -1
        for i, num in enumerate(nums):
            mx = max(mx, right_most[num])
            if i == mx:
                group_cnt += 1
        return pow(2, group_cnt - 1, MOD)

