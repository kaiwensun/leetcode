from collections import Counter

class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = Counter(s)
        if cnt["0"] == cnt["1"]:
            starts = "01"
        elif cnt["0"] == cnt["1"] + 1:
            starts = "0"
        elif cnt["0"] + 1 == cnt["1"]:
            starts = "1"
        else:
            return -1
        res = float("inf")
        for desired in starts:
            diff = 0
            for c in s:
                diff += int(c != desired)
                desired = "1" if desired == "0" else "0"
            res = min(res, diff)
        return res // 2

