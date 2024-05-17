class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = energy[-1]
        for start in range(len(energy) - 1, len(energy) - 1 - k, -1):
            sm = 0
            for i in range(start, -1, -k):
                sm += energy[i]
                res = max(res, sm)
        return res

