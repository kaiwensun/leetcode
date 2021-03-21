import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        gcd = lru_cache(None)(math.gcd)
        get_index = lru_cache(None)(lambda mask: int(math.log2(mask)))

        def get_highest_bit(mask):
            for shift in 1, 2, 4, 8:
                mask |= mask >> shift
            return (mask + 1) >> 1


        @lru_cache(None)
        def dp(i, remaining):
            inrem = remaining
            if i > len(nums) // 2:
                return 0
            mask1 = remaining
            res = 0
            while mask1:
                bit1 = get_highest_bit(mask1)
                mask1 ^= bit1
                num1 = nums[get_index(bit1)]
                mask2 = mask1
                while mask2:
                    bit2 = get_highest_bit(mask2)
                    mask2 ^= bit2
                    num2 = nums[get_index(bit2)]
                    res = max(res, gcd(num1, num2) * i + dp(i + 1, remaining ^ bit1 ^ bit2))
            return res
        nums.sort()
        return dp(1, (1 << len(nums)) - 1)

