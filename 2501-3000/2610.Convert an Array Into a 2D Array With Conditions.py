class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = None
        res = []
        for num in nums:
            if num != prev:
                row = 0
            if row == len(res):
                res.append([])
            res[row].append(num)
            row += 1
            prev = num
        return res

