class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x_char = str(x)
        if n[0] == "-":
            for i in range(1, len(n)):
                if n[i] > x_char:
                    return n[:i] + x_char + n[i:]
        else:
            for i in range(len(n)):
                if n[i] < x_char:
                    return n[:i] + x_char + n[i:]
        return n + x_char

