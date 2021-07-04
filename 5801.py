class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i, minute in enumerate(sorted(dist[i]/speed[i] for i in range(len(dist)))):
            if i >= minute:
                return i
        return len(dist)

