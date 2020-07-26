import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = [float("-inf")] * k
        for num in nums:
            heapq.heappushpop(queue, num)
        return queue[0]
