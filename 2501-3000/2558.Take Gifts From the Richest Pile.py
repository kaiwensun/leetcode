import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            g = heapq.heappop(gifts)
            g = -int(math.sqrt(-g))
            heapq.heappush(gifts, g)
        return sum(-g for g in gifts)

