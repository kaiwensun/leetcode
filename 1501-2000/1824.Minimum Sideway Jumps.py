class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [1, 0, 1]
        for i in range(1, n):
            new_dp = [
                min(
                    dp[prev] + (prev != j) + (obstacles[i] - 1 == prev and float("inf"))
                    for prev in range(3)
                )
                + (obstacles[i] and obstacles[i] - 1 == j and float("inf")) for j in range(3)
            ]
            dp = new_dp
        return min(dp)

