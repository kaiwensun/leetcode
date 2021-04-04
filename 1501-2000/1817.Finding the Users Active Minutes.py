from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        counter = defaultdict(set)
        for i, t in logs:
            counter[i].add(t)
        res = [0] * k
        for _, tsize in counter.items():
            if len(tsize) <= k:
                res[len(tsize) - 1] += 1
        return res

