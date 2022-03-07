class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, row1, _, col2, row2 = list(s)
        return [chr(col) + chr(row) for col in range(ord(col1), ord(col2) + 1) for row in range(ord(row1), ord(row2) + 1)]

