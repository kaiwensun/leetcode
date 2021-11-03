class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        first_events = [[0, 0]]  # [end time, value of first event]
        for start, end, value in sorted(events, key=lambda event: (event[1], -event[2])):
            if end != first_events[-1][0]:
                first_events.append([end, max(value, first_events[-1][1])])

        second_events = [[float("inf"), 0]]  # [start time, value of second event]
        for start, end, value in sorted(events, key=lambda event: (-event[0], -event[2])):
            if start != second_events[-1][0]:
                second_events.append([start, max(value, second_events[-1][1])])
        res = 0
        j = len(second_events) - 1
        for first_event in first_events:
            while second_events[j][0] <= first_event[0]:
                j -= 1
            res = max(res, first_event[1] + second_events[j][1])
        return res

