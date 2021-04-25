class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n])
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + restrictions[i][0] - restrictions[i - 1][0])
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + restrictions[i + 1][0] - restrictions[i][0])
        res = 0
        for i in range(len(restrictions) - 1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            res = max(res, restrictions[i + 1][1] + (restrictions[i][1] + dist - restrictions[i + 1][1]) // 2)
        return res

