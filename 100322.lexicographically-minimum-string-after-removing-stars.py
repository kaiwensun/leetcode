import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i, c in enumerate(s):
            if c == '*':
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, (c, -i))
        heap.sort(key = lambda item: -item[1])
        return ''.join(item[0] for item in heap)

