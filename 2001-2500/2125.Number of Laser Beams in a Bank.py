from collections import Counter

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = prev = 0
        for row in bank:
            cnt = Counter(row)
            if cnt['1']:
                res += prev * cnt['1']
                prev = cnt['1']
        return res

