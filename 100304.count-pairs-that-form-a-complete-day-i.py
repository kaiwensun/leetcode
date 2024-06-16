from itertools import combinations
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        return sum(1 for a, b in combinations(hours, 2) if (a + b) % 24 == 0)

