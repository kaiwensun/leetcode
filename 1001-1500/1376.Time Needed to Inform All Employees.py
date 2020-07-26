import functools
class Solution:
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @functools.lru_cache(n)
        def cost(index):
            if index == headID:
                return 0
            return informTime[manager[index]] + cost(manager[index])
        return max(cost(i) for i in range(n))
