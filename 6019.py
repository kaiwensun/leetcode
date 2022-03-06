import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(num)
            while len(res) >= 2 and math.gcd(res[-2], res[-1]) != 1:
                num1, num2 = res.pop(), res.pop()
                res.append(num1 * num2 // math.gcd(num1, num2))
        return res

