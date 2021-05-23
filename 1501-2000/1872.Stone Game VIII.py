class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        diff = prefix = sum(stones)
        for i in range(len(stones) - 2, 0, -1):
            prefix -= stones[i + 1]
            diff = max(prefix - diff, diff)
        return diff

