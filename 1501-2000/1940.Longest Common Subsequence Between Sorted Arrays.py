import heapq

class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        res = []
        N = len(arrays)
        heap = [(arrays[i][0], i, 0) for i in range(N)]
        heapq.heapify(heap)
        heap.append((float("inf"), N, 0))
        candidate = candidate_cnt = None
        while True:
            num, i, j = heapq.heappop(heap)
            if num == candidate:
                candidate_cnt += 1
            else:
                if len(heap) != N:
                    break
                candidate_cnt = 1
                candidate = num
            if candidate_cnt == N:
                res.append(candidate)
            j += 1
            if j < len(arrays[i]):
                heapq.heappush(heap, (arrays[i][j], i, j))
        return res

