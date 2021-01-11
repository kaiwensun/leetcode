class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        @lru_cache(None)
        def available_jobs(todo_bitmap, i):
            while (1 << i) & todo_bitmap == 0 and i < len(jobs):
                i += 1
            if i == len(jobs):
                return [(0, 0)]
            else:
                res = []
                for my_jobs, my_cost in available_jobs(todo_bitmap, i + 1):
                    res.append((my_jobs, my_cost))
                    res.append(((my_jobs | (1 << i)), my_cost + jobs[i]))
                return res

        def next_available_job(todo_jobs):
            for i in range(len(jobs)):
                if (1 << i) & todo_jobs != 0:
                    return i
                
        @lru_cache(None)
        def dp(todo_bitmap, worker_id):
            if worker_id == k:
                if todo_bitmap == 0:
                    return 0
                else:
                    return float("inf")
            if todo_bitmap == 0:
                return 0
            res = float("inf")
            i = next_available_job(todo_bitmap)
            todo_bitmap -= 1 << i
            
            for my_jobs, my_cost in available_jobs(todo_bitmap, i + 1):
                if my_cost + jobs[i] > res:
                    continue
                next_todo_bitmap = todo_bitmap - my_jobs
                res = min(res, max(my_cost + jobs[i], dp(next_todo_bitmap, worker_id + 1)))
            return res
        res = dp((1 << len(jobs)) - 1, 0)
        dp.cache_clear()
        available_jobs.cache_clear()
        return res

