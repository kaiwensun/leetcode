from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = len(set(nums))
        cnt = Counter()
        l = 0
        res = 0
        for r in range(len(nums)):
            cnt[nums[r]] += 1
            if len(cnt) == unique:
                while len(cnt) == unique:
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        del cnt[nums[l]]
                    l += 1
                res += l
            elif res:
                res += l
        return res

