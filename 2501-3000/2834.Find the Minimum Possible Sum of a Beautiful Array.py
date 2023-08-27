class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        i = 1
        seen = set()
        while len(seen) < n:
            if target - i not in seen:
                seen.add(i)
            i += 1
        return sum(seen)

