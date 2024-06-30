from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = Counter()
        for hour in hours:
            cnt[hour % 24] += 1
        res = 0
        for hour in range(13):
            if hour % 12:
                res += cnt[hour] * cnt[24 - hour]
            else:
                res += cnt[hour] * (cnt[hour] - 1) // 2
        return res

