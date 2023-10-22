class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_rights = [float("inf")]
        for num in reversed(nums):
            min_rights.append(min(min_rights[-1], num))
        min_rights.reverse()
        min_rights.pop()

        numi = nums[0]
        res = float("inf")
        for j in range(1, len(nums) - 1):
            numj = nums[j]
            if numi < numj > min_rights[j + 1]:
                res = min(res, numi + numj + min_rights[j + 1])
            numi = min(numi, numj)
        return -1 if res == float("inf") else res

