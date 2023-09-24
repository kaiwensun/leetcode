class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def calc(i):
            res = 0
            mx = maxHeights[i]
            for j in range(i - 1, -1, -1):
                mx = min(mx, maxHeights[j])
                res += mx
            mx = maxHeights[i]
            for j in range(i, len(maxHeights)):
                mx = min(mx, maxHeights[j])
                res += mx
            return res
        return max(calc(i) for i in range(len(maxHeights)))

