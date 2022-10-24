class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def total_cost(avg):
            return sum(abs(n - avg) * c for (n, c) in zip(nums, cost))
        left, right = MN, MX = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            lres = float("inf") if mid == MN else total_cost(mid - 1)
            mres = total_cost(mid)
            rres = float("inf") if mid == MX else total_cost(mid + 1)
            if lres < mres:
                right = mid - 1
            elif rres < mres:
                left = mid + 1
            else:
                left = right = mid
        return total_cost(left)

