import heapq

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        sm = sum(num for num in nums if num > 0)
        nums = sorted((num if num < 0 else -num for num in nums), reverse=True)
        n = len(nums)
        nums.append(0)
        heap = [(-sm, -1)]
        for _ in range(k - 1):
            s, i = heapq.heappop(heap)
            if i + 1 < n:
                heapq.heappush(heap, (s + nums[i] - nums[i + 1], i + 1))
                if i != -1:
                    heapq.heappush(heap, (s - nums[i + 1] , i + 1))
        return -heap[0][0]


