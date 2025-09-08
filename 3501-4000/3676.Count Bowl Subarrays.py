class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        res = 0
        desc = []
        for r, num in enumerate(nums):
            while desc and desc[-1][0] < num:
                prev, l = desc.pop()
                if l != r - 1:
                    res += 1
            if desc and desc[-1][1] != r - 1:
                res += 1
            if desc and desc[-1][0] == num:
                desc.pop()
            desc.append((num, r))
        return res

