from collections import deque
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter(basket1) + Counter(basket2)
        for value in cnt.values():
            if value % 2 == 1:
                return -1
        n = len(basket1)
        basket1.sort()
        basket2.sort()
        candidates1 = deque()
        candidates2 = deque()
        stay = None
        i = j = 0
        while i < n and j < n:
            if basket1[i] == basket2[j]:
                if stay is None:
                    stay = basket1[i]
                i += 1
                j += 1
            elif basket1[i] < basket2[j]:
                candidates1.append(basket1[i])
                i += 1
            else:
                candidates2.append(basket2[j])
                j += 1
        if i < n:
            candidates1.extend(basket1[i:])
        if j < n:
            candidates2.extend(basket2[j:])
        
            
        if stay is None:
            stay = float("inf")
        res = 0
        while candidates1 and candidates2:
            c1 = candidates1[0]
            c2 = candidates2[0]
            if stay is not None and stay * 2 < min(c1, c2):
                res += stay * len(candidates1)
                break
            elif c1 < c2:
                res += c1
                candidates1.popleft()
                candidates1.popleft()
                candidates2.pop()
                candidates2.pop()
                stay = min(stay, c1)
            else:
                res += c2
                candidates1.pop()
                candidates1.pop()
                candidates2.popleft()
                candidates2.popleft()
                stay = min(stay, c2)
        return res

