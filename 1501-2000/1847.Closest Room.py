import heapq
from sortedcontainers import SortedList

class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        queries = [(min_size, preferred, qid) for qid, (preferred, min_size) in enumerate(queries)]
        queries.sort(reverse=True)
        rooms = list(sorted(map(tuple, map(reversed, rooms))))
        answers = []
        room_ptr = len(rooms) - 1
        available_room_ids = SortedList()
        for min_size, preferred, qid in queries:
            while room_ptr >= 0 and rooms[room_ptr][0] >= min_size:
                available_room_ids.add(rooms[room_ptr][1])
                room_ptr -= 1
            if available_room_ids:
                i = available_room_ids.bisect_right(preferred)
                room_id1, room_id2 = available_room_ids[i - 1], available_room_ids[min(i, len(available_room_ids) - 1)]
                answers.append((qid, room_id1 if abs(room_id1 - preferred) <= abs(room_id2 - preferred) else room_id2))
            else:
                answers.append((qid, -1))
        answers.sort()
        return [ans for qid, ans in answers]

