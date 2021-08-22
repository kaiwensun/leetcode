class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        n = len(nums)
        nums = set(nums)
        for i in range(n):
            if not nums:
                break
            to_remove = set()
            num = nums.pop()
            res.append('1' if num[i] == '0' else '0')
            for num2 in nums:
                if num2[i] == num[i]:
                    to_remove.add(num2)
            nums -= to_remove
        res.append("0" * (n - len(res)))
        return ''.join(res)

