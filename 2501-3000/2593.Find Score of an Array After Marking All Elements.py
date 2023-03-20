class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False] * (len(nums) + 2)
        res = 0
        for i, num in sorted(enumerate(nums), key=lambda x: tuple(reversed(x))):
            if marked[i] or marked[i + 1] or marked[i - 1]: continue
            marked[i] = True
            res += num
        return res

