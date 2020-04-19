
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def cntOptions(index):
            """
            Given the chars at `0..index`, how many different strings are there
            """
            return 1 << (n - index - 1)
        prev_char = ""
        res = []
        for i in range(n):
            for char in "abc":
                if prev_char == char:
                    continue
                if k - cntOptions(i) > 0:
                    k -= cntOptions(i)
                else:
                    prev_char = char
                    res.append(char)
                    break
        return "".join(res) if len(res) == n else ""
