import heapq

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        heap = [(-num, index) for index, num in enumerate(nums2)]
        heapq.heapify(heap)
        res = 0
        print(heap)
        for i in range(len(nums1)):
            while heap and nums1[i] <= -heap[0][0]:
                if i <= heap[0][1]:
                    res = max(res, heap[0][1] - i)
                heapq.heappop(heap)
        return res

