import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            num = -heapq.heappop(nums)
            res += num
            heapq.heappush(nums, -((num + 2) // 3))
        return res

