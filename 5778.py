class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = float("inf")
        for wanted in "01":
            mismatched = 0
            flip_mismatched = 0
            for bit in s:
                if wanted != bit:
                    mismatched += 1
                elif len(s) % 2:
                    flip_mismatched = min(flip_mismatched + 1, mismatched)
                wanted = "1" if wanted == "0" else "0"
            res = min(res, mismatched, flip_mismatched if len(s) % 2 else float("inf"))
        return res

