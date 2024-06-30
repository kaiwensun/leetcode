class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        for parities in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cur = 0
            for num in nums:
                if num % 2 == parities[cur % 2] % 2:
                    cur += 1
            res = max(cur, res)
        return res

