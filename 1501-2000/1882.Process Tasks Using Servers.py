import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        task_id = time = 0
        processing = [] # [(ending_time, task_id, server_id), ...]
        available = [(weight, server_id) for server_id, weight in enumerate(servers)]
        heapq.heapify(available)
        ans = [None] * len(tasks)
        while task_id < len(tasks):
            while processing and processing[0][0] <= time:
                ending_time, server_id = heapq.heappop(processing)
                heapq.heappush(available, (servers[server_id], server_id))
            if not available:
                time = processing[0][0]
                continue
            time = max(time, task_id)
            while task_id <= time and task_id < len(tasks) and available:
                weight, server_id = heapq.heappop(available)
                heapq.heappush(processing, (time + tasks[task_id], server_id))
                ans[task_id] = server_id
                task_id += 1
            time = max(time, task_id)
        return ans

