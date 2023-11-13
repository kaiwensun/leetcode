from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def parse_time(t):
            return 60 * int(t[:2]) + int(t[2:])
        employees = defaultdict(list)
        for name, t in access_times:
            employees[name].append(parse_time(t))
        res = []
        for name, times in employees.items():
            times.sort()
            for i in range(len(times) - 2):
                if times[i + 2] - times[i] < 60:
                    res.append(name)
                    break
        return res

