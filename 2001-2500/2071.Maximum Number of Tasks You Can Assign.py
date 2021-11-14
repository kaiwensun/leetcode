from sortedcontainers import SortedList

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        N = min(len(tasks), len(workers))
        tasks = sorted(tasks)[:N]
        workers = sorted(workers)[-N:]

        def test(n):
            p = pills
            sub_tasks = SortedList(tasks[:n])
            sub_workers = workers[-n:]
            for i, worker in enumerate(sub_workers):
                if sub_tasks[0] <= worker:
                    sub_tasks.pop(0)
                    continue
                else:
                    if p == 0:
                        return False
                    p -= 1
                    j = sub_tasks.bisect_right(worker + strength) - 1
                    if j == -1:
                        return False
                    sub_tasks.pop(j)
            return True


        l, r = 0, N + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

