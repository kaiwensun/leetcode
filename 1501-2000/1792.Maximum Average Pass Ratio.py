import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def item(pas, total):
            return ((pas / total) - (pas + 1) / (total + 1), pas, total)
        heap = [item(pas, total) for pas, total in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            delta, pas, total = heap[0]
            heapq.heapreplace(heap, item(pas + 1, total + 1))
        sm = sum(pas / total for delta, pas, total in heap)
        return sm / len(heap)

