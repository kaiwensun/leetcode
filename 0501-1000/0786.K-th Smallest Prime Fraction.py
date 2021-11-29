import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [[1 / arr[j], 0, j] for j in range(1, len(arr))] # [fraction, i, j]
        heapq.heapify(heap)
        for _ in range(k - 1):
            heap[0][0] = arr[heap[0][1] + 1] / arr[heap[0][2]]
            heap[0][1] += 1
            heapq.heapreplace(heap, heap[0])
        return [arr[heap[0][1]], arr[heap[0][2]]]

