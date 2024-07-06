from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [num % k for num in nums]
        prev_index = defaultdict(lambda: -1)
        prevs = []
        for i, num in enumerate(nums):
            prevs.append(prev_index[num])
            prev_index[num] = i
        res = 0
        presence = list(set(nums))
        for num1 in presence:
            for num2 in presence:
                i1 = prev_index[num1]
                i2 = prev_index[num2]
                size = 1
                while True:
                    while i2 >= i1:
                        i2 = prevs[i2]
                    if i2 == -1:
                        break
                    size += 1
                    while i1 >= i2:
                        i1 = prevs[i1]
                    if i1 == -1:
                        break
                    size += 1
                res = max(res, size)
        return res

