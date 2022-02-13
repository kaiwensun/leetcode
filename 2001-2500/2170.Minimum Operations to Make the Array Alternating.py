from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 2 and nums[0] == nums[1]:
            return 1
        if len(nums) <= 2:
            return 0
        cnt1 = Counter(nums[0::2]).most_common(2)
        cnt2 = Counter(nums[1::2]).most_common(2)
        if cnt1[0][0] != cnt2[0][0]:
            return len(nums) - cnt1[0][1] - cnt2[0][1]
        if len(cnt1) == len(cnt2) == 1:
            return cnt2[0][1]
        if len(cnt1) == 1:
            return len(nums) - cnt1[0][1] - cnt2[1][1]
        if len(cnt2) == 1:
            return len(nums) - cnt2[0][1] - cnt1[1][1]
        return len(nums) - max(
            cnt1[0][1] + cnt2[1][1],
            cnt2[0][1] + cnt2[1][1]
        )

