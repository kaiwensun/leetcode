class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs.append(0)
        res = 0
        for i in range(len(rungs) - 1):
            res += (rungs[i] - 1 - rungs[i - 1]) // dist
        return res

