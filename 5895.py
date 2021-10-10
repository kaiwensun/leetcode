from collections import Counter

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        cnt = Counter()
        for row in grid:
            for num in row:
                cnt[num] += 1
        stats = sorted(cnt.items())
        lcost = rcost = 0
        base = stats[0][0]
        for num, c in stats:
            if (num - base) % x != 0:
                return -1
            rcost += c * (num - base) // x
        res = rcost
        lsize, rsize = 0, len(grid) * len(grid[0])
        i = 0
        cost = float("inf")
        for target in range(base, stats[-1][0] + x, x):
            cost = min(cost, lcost + rcost)
            if stats[i][0] == target:
                rsize -= stats[i][1]
                lsize += stats[i][1]
                i += 1
            lcost += lsize
            rcost -= rsize
        return cost

