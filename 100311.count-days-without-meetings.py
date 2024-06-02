class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = 0
        cur = 0
        for start, end in meetings:
            if start > cur:
                res += start - cur - 1
            cur = max(cur, end)
        res += days - cur
        return res

