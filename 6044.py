class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:        # [time, is_end]
        events = []
        for start, end in flowers:
            events.append((start, False))
            events.append((end, True))
        events.sort()
        persons = sorted((p, i) for (i, p) in enumerate(persons))
        answer = [0] * len(persons)
        cnt = 0
        event_id = 0
        for p, i in persons:
            while event_id < len(events) and (events[event_id][0] < p or (events[event_id][0] == p and events[event_id][1] == False)):
                if events[event_id][1]:
                    cnt -= 1
                else:
                    cnt += 1
                event_id += 1
            answer[i] = cnt
        return answer

