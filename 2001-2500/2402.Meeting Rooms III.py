import heapq, collections

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_cnt = collections.Counter()
        available_roomes = list(range(n))  # [room_id, ...]
        heapq.heapify(available_roomes)
        meetings.sort(reverse=True)  # [[start, end], ...]
        pending_meetings = collections.deque()  # [time_length, ...]
        inprogress_meetings = []  # [[end_time, room_id], ...]
        t = meetings[-1][0]
        while meetings or pending_meetings:
            while inprogress_meetings and inprogress_meetings[0][0] == t:
                _, room_id = heapq.heappop(inprogress_meetings)
                heapq.heappush(available_roomes, room_id)
            while meetings and meetings[-1][0] <= t:
                start, end = meetings.pop()
                pending_meetings.append(end - start)
            while pending_meetings and available_roomes:
                room_id = heapq.heappop(available_roomes)
                time_length = pending_meetings.popleft()
                heapq.heappush(inprogress_meetings, [t + time_length, room_id])
                room_cnt[room_id] += 1
            t = min(
                meetings[-1][0] if meetings else float("inf"),
                inprogress_meetings[0][0] if inprogress_meetings else float("inf"))
        return -heapq.nlargest(3,((cnt, -room_id) for (room_id, cnt) in room_cnt.items()))[0][1]

