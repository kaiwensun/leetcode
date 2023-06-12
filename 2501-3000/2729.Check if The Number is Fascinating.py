class Solution:
    def isFascinating(self, n: int) -> bool:
        num = "".join(str(n * i) for i in range(1, 4))
        return len(num) == len(set(num)) == 9 and '0' not in num

