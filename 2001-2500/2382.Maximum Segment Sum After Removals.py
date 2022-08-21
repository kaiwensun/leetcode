import collections, heapq, sortedcontainers

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        heap = [-prefix[-1], 0]
        pending_delete = collections.Counter()
        segments = sortedcontainers.SortedList([(0, len(nums))])
        res = []

        for query in removeQueries:
            split_point = segments.bisect_right((query, float("inf"))) - 1
            start, end = segments.pop(split_point)
            pending_delete[prefix[end] - prefix[start]] += 1
            start1, end1, start2, end2 = start, query, query + 1, end
            if start1 != end1:
                segments.add((start1, end1))
                heapq.heappush(heap, prefix[start1] - prefix[end1])
            if start2 != end2:
                segments.add((start2, end2))
                heapq.heappush(heap, prefix[start2] - prefix[end2])
            while pending_delete[-heap[0]]:
                pending_delete[-heapq.heappop(heap)] -= 1
            res.append(-heap[0])
        return res

