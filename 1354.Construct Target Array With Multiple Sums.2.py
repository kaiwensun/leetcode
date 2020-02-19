import heapq
class Solution(object):
    def isPossible(self, target):
        s = sum(target)
        max_heap = [-t for t in target]
        heapq.heapify(max_heap)
        while max_heap[0] != -1:
            top = -heapq.heappop(max_heap)
            snd = -max_heap[0] if max_heap else 0
            restored = top * 2 - s
            diff = top - restored
            if top == snd or diff == 0:
                return False
            restored = snd + (top - snd) % -diff
            if restored < 1:
                return False
            s -= (top - restored)
            heapq.heappush(max_heap, -restored)
        return True
