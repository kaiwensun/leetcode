import functools, collections, bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        end2eid = collections.defaultdict(list)
        for i in range(len(events)):
            end2eid[events[i][1]].append(i)
        end_days = list(sorted(end2eid.keys()))

        @functools.lru_cache(None)
        def dp(end_day_index, count):
            if count == 0 or end_day_index == -1:
                return 0
            res = dp(end_day_index - 1, count)
            for eid in end2eid[end_days[end_day_index]]:
                start, end, value = events[eid]
                res = max(res, dp(bisect.bisect_left(end_days, start) - 1, count - 1) + value)
            return res
        return dp(len(end_days) - 1, k)

