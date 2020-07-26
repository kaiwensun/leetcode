class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        num1 = num + 1
        num2 = num + 2
        mx = int(math.sqrt(num2))

        for a in range(mx, 0, -1):
            if num1 % a == 0:
                return [a, num1 // a]
            if num2 % a == 0:
                return [a, num2 // a]
        assert(False)
