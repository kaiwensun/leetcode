import math

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        first_seen = {}
        skip_to = list(range(len(nums)))
        for i, num in enumerate(nums):
            first_seen.setdefault(num, i)
            skip_to[first_seen[num]] = i

        left = 1
        lefts = []
        for num in nums:
            left = math.lcm(left, num)
            lefts.append(left)

        right = 1
        rights = []
        for num in reversed(nums):
            right = math.lcm(right, num)
            rights.append(right)
        rights.reverse()

        i = 0
        while i < len(nums) - 1:
            if skip_to[i] != i:
                i = skip_to[i]
                continue
            if math.gcd(lefts[i], rights[i + 1]) == 1:
                return i
            i += 1
        return -1

