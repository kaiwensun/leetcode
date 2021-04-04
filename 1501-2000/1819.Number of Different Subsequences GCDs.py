import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        num = set(nums)
        mx = max(nums)
        return sum(candidate == math.gcd(
            *(multi for multi in range(candidate, mx + 1, candidate) if multi in num)
        ) for candidate in range(1, mx + 1))

