from functools import cache

@cache
def dp(n, p1, p2):
    p2_competator = competator(p2, n)
    if p1 == p2_competator:
        return 1, 1
    p1, p2 = min(p1, p2), max(p1, p2)
    if p1 >= n // 2 or (p2 >= (n + 1) // 2 and p1 > p2_competator):
        return dp(n, p2_competator, competator(p1, n))
    if p2 < (n + 1) // 2:
        delta_p2_range = 1, 1 + p2 - p1
    else:
        delta_p2_range = (n + 1) // 2 - p2_competator, (n + 1) // 2 - p1
    min_cost, max_cost = float("inf"), -1
    for new_p1 in range(p1 + 1):
        for delta_p2 in range(*delta_p2_range):
            subres = dp((n + 1) // 2, new_p1, new_p1 + delta_p2)
            min_cost = min(min_cost, subres[0] + 1)
            max_cost = max(max_cost, subres[1] + 1)
    return min_cost, max_cost

def competator(i, n):
    return n - i - 1

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        return dp(n, firstPlayer - 1, secondPlayer - 1)

