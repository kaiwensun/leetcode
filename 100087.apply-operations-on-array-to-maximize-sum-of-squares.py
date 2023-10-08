MOD = 10 ** 9 + 7

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mask = 1
        array = [0] * k
        while mask < MOD:
            i = 0
            for num in nums:
                bit = mask & num
                if bit:
                    array[i] |= bit
                    i += 1
                    if i == len(array):
                        break
            mask <<= 1
        res = 0
        for a in array:
            res += a * a
            res %= MOD
        return res

