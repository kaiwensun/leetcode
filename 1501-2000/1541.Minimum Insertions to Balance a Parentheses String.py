class Solution:
    def minInsertions(self, s: str) -> int:
        # states = ["", "(", "()"]
        state = ""
        res, opened = 0, 0
        i = 0
        for c in s:
            if c == "(":
                if state == "()":
                    res += 1
                opened += 1
                state = "(" if opened else ""
            else:  # ")"
                if state == "":
                    res += 1
                    state = "()"
                elif state == "(":
                    opened -= 1
                    state = "()"
                else:
                    state = "(" if opened else ""
            i += 1
        if state == "()":
            res += 1
        return res + opened * 2

