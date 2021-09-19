from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        debt = Counter()
        res = []
        for num in changed:
            if debt[num]:
                debt[num] -= 1
            else:
                debt[num * 2] += 1
                res.append(num)
        if debt and max(debt.values()):
            return []
        return res

