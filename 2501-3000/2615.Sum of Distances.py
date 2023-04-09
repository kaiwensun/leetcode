from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        num2i = defaultdict(list)
        for i, num in enumerate(nums):
            num2i[num].append(i)
        arr = [0] * len(nums)
        for ilist in num2i.values():
            if len(ilist) == 1:
                continue
            ilist.sort()
            l = 0
            r = sum(ilist)
            for j, i in enumerate(ilist):
                r -= i
                arr[i] = r - l - i * (len(ilist) - j - j - 1)
                l += i
        return arr

