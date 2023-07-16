from collections import deque

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        queue = deque()
        res = 0
        for num in sorted(nums):
            while queue and queue[0] < num - k * 2:
                queue.popleft()
            queue.append(num)
            res = max(res, len(queue))
        return res

