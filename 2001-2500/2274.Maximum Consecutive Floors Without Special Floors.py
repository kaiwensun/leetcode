class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.extend([top + 1, bottom - 1])
        special.sort()
        res = 0
        for a, b in zip(special[: - 1], special[1:]):
            res = max(res, b - a - 1)
        return res

