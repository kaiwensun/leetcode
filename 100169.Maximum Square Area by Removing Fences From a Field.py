MOD = 10 ** 9 + 7
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        def getEdges(fences, l):
            fences.append(1)
            fences.append(l)
            fences.sort()
            res = []
            for i in range(len(fences)):
                for j in range(i + 1, len(fences)):
                    res.append(fences[j] - fences[i])
            return sorted(res)
        hEdges, vEdges = getEdges(hFences, m), getEdges(vFences, n)
        while hEdges and vEdges:
            if hEdges[-1] == vEdges[-1]:
                return (hEdges[-1] ** 2) % MOD
            if hEdges[-1] > vEdges[-1]:
                hEdges.pop()
            else:
                vEdges.pop()
        return -1

