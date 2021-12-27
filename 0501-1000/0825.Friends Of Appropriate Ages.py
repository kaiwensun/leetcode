from collections import Counter
from bisect import bisect_left

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def count_range(start, end):
            if start >= end:
                return 0
            start_i = bisect_left(keys, start)
            end_i = bisect_left(keys,  end)
            return pre_sum[end_i] - pre_sum[start_i]

        cnt = Counter(ages)
        keys = sorted(cnt.keys())
        pre_sum = [0]
        res = 0
        for key in keys:
            pre_sum.append(pre_sum[-1] + cnt[key])
        for start in keys:
             # start is y
             # end is x
             # no matter y is greater than or less than 100,
             # for y to receive a request, we always have x < 2y - 14 and x >= y
            end = 2 * start - 14
            requests = count_range(start, end)
            if start < end and start in cnt:
                res += cnt[start] * (requests - 1)
            else:
                res += requests
        return res

