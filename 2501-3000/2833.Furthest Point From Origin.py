from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        def dist(fill):
            cnt = Counter(moves.replace("_", fill))
            return abs(cnt["L"] - cnt["R"])
        return max(dist("L"), dist("R"))

