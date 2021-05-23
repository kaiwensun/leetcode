class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        farthest = 0
        reached = [False] * len(s)
        reached[0] = True
        for i in range(len(s)):
            if not reached[i]:
                continue
            for j in range(max(i + minJump, farthest + 1), min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    reached[j] = True
            farthest = j
        return reached[-1]

