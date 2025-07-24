from collections import Counter

class Solution:
    MOD = 10 ** 9 + 7
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points_cnt = Counter()
        for x, y in points:
            points_cnt[y] += 1
        pairs_cnt = {k: v * (v - 1) // 2 for k, v in points_cnt.items()}
        pairs_sum = sum(pairs_cnt.values())
        res = 0
        for row_cnt in pairs_cnt.values():
            pairs_sum -= row_cnt
            res += row_cnt * pairs_sum
            res %= Solution.MOD
        return res

