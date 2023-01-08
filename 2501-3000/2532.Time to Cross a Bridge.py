import heapq

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        def get_worker(i):
            return [-time[i][0] - time[i][2], -i]

        left_bridge, picking, right_bridge, putting = [get_worker(i) for i in range(k)], [], [], []
        heapq.heapify(left_bridge)
        now = 0
        left_box = 0
        worker_sent = 0
        while True:
            while picking and picking[0][0] <= now:
                t, worker = heapq.heappop(picking)
                heapq.heappush(right_bridge, get_worker(worker))
            while putting and putting[0][0] <= now:
                t, worker = heapq.heappop(putting)
                heapq.heappush(left_bridge, get_worker(worker))
            if right_bridge:
                _, neg_i = heapq.heappop(right_bridge)
                now += time[-neg_i][2]
                left_box += 1
                if left_box == n:
                    return now
                heapq.heappush(putting, [now + time[-neg_i][3], -neg_i])
            elif left_bridge and worker_sent < n:
                _, neg_i = heapq.heappop(left_bridge)
                now += time[-neg_i][0]
                heapq.heappush(picking, [now + time[-neg_i][1], -neg_i])
                worker_sent += 1
            else:
                pick_t = picking[0][0] if picking else float("inf")
                put_t = putting[0][0] if putting else float("inf")
                now = min(pick_t, put_t)

