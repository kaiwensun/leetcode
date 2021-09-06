from sortedcontainers import SortedList

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        M, N = len(land), len(land[0])
        pending = SortedList([[float("inf")] * 4], key=lambda farm: farm[1])
        res = []
        for i in range(M + 1):
            j = 0
            next_farm = pending[0]
            while j < N:
                if j == next_farm[1]:
                    if i != M and land[i][j] == 1:
                        j = next_farm[3] + 1
                        next_farm = pending[pending.bisect_left([None, j])]
                    else:
                        pending.remove(next_farm)
                        next_farm[2] = i - 1
                        res.append(next_farm)
                        next_farm = pending[pending.bisect(next_farm)]
                else:
                    if i != M and land[i][j] == 1:
                        new_farm = [i, j, None, None]
                        while j < N and land[i][j] == 1:
                            j += 1
                        j -= 1
                        new_farm[3] = j
                        pending.add(new_farm)
                    else:
                        pass
                j += 1
        return res

