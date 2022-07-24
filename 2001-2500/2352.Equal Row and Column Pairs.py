from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(map(tuple, grid))
        columns = Counter(map(tuple, zip(*grid)))
        return sum(rows[key] * columns[key] for key in set(rows.keys()))


