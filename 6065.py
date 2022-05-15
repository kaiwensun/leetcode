class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        MAX = 10 ** 7
        mask = 1
        res = 0
        while mask <= MAX:
            res = max(res, sum(1 for _ in filter(lambda cand: cand & mask, candidates)))
            mask <<= 1
        return res

