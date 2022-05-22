class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        for space in sorted([c - r for (c, r) in zip(capacity, rocks)]):
            additionalRocks -= space
            if additionalRocks >= 0:
                res += 1
            else:
                break
        return res

