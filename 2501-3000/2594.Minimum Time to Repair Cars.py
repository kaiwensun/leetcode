import heapq

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # [[r * (n + 1) ^ 2, r * n ^ 2, r, n], ...]
        powers = [[r, 0, r, 0] for r in ranks]
        heapq.heapify(powers)
        for _ in range(cars):
            nxt_rn2, rn2, r, n = powers[0]
            heapq.heapreplace(powers, [nxt_rn2 + r * (n * 2 + 3), nxt_rn2, r, n + 1])
        return max(p[1] for p in powers)

