import collections

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        sm = sum(piles)
        processed = collections.deque()
        piles.sort()
        for _ in range(k):
            if not (piles or processed):
                break
            num1 = piles.pop() if piles else 0
            num2 = processed.pop() if processed else 0
            if num1 > num2:
                diff = num1 // 2
                num1 -= diff
                sm -= diff
                processed.appendleft(num1)
                if num2 != 0:
                    processed.append(num2)
            else:
                diff = num2 // 2
                num2 -= diff
                sm -= diff
                if num2 != 0:
                    processed.appendleft(num2)
                if num1 != 0:
                    piles.append(num1)
        return sm

