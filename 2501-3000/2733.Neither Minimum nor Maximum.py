class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
            if len(seen) == 3:
                mn, mx = min(seen), max(seen)
                seen.remove(mn)
                seen.remove(mx)
                return seen.pop()
        return -1

