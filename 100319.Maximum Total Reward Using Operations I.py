class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        possible_sums = set()
        for r in rewardValues:
            possible_sums |= {r + x for x in possible_sums if r > x} | {r}
        return max(possible_sums)

