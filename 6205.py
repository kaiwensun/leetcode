class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums) | set(int(''.join(reversed(str(num)))) for num in nums))

