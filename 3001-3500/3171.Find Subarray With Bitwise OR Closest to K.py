class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        s = set()
        res = float("inf")
        for num in nums:
            s = {num | prev for prev in s} | {num}
            res = min(res, min(abs(n - k) for n in s))
        return res

