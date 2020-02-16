import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # sort according to start time
        events = sorted(events)
        total_days = max(event[1] for event in events)
        min_heap = []
        day = 1
        cnt = 0
        event_id = 0
        while day <= total_days:
            if event_id < len(events) and not min_heap:
                day = max(day, events[event_id][0])
            while event_id < len(events) and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                cnt += 1
            day += 1
        return cnt
