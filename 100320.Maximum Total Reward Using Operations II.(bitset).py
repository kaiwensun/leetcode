class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        possible_sums = 0
        for r in rewardValues:
            smallers = possible_sums & (1 << r) - 1
            possible_sums |= (smallers | 1) << r
        return possible_sums.bit_length() - 1

