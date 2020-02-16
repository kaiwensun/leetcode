import heapq
class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        s = sum(target)
        max_heap = [-t for t in target]
        heapq.heapify(max_heap)
        while max_heap[0] != -1:
            restored = s - (s + max_heap[0]) * 2
            if restored < 1 or max_heap[0] == -restored:
                return False
            s += max_heap[0] + restored
            heapq.heapreplace(max_heap, -restored)
        return True
