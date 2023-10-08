class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        p_iter = iter(sorted(processorTime))
        t_iter = iter(sorted(tasks, reverse=True))
        res = 0
        while (p := next(p_iter, None)) is not None:
            t = max(next(t_iter), next(t_iter), next(t_iter), next(t_iter))
            res = max(res, t + p)
        return res

