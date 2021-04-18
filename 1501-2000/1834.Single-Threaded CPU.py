import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [(task[0], task[1], task_id) for task_id, task in enumerate(tasks)]
        tasks.sort()
        task_itr = iter(tasks)
        res, heap = [], []
        task = next(task_itr)
        cur_time = task[0]
        for _ in range(n):
            if not heap:
                cur_time = max(cur_time, task[0])
            while task and cur_time >= task[0]:
                heapq.heappush(heap, (task[-2:]))
                task = next(task_itr, None)
            processing_time, task_id = heapq.heappop(heap)
            cur_time += processing_time
            res.append(task_id)
        return res

