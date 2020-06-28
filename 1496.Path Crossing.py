class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = (0, 0)
        seen = {cur}
        deltamap = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }
        for step in path:
            delta = deltamap[step]
            cur = (cur[0] + delta[0], cur[1] + delta[1])
            if cur in seen:
                return True
            seen.add(cur)
        return False
