class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        seen = set(range(n))
        for _, v in edges:
            if v in seen:
                seen.remove(v)
        return seen.pop() if len(seen) == 1 else -1

