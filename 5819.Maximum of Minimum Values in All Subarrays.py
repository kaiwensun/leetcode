class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.append(float("-inf"))
        expansion = [None] * N
        inc_stack = [-1]
        for i, num in enumerate(nums):
            while nums[inc_stack[-1]] > num:
                j = inc_stack.pop()
                expansion[j] = i - inc_stack[-1] - 2
            inc_stack.append(i)
        sorted_expansion = sorted(((expan, i) for i, expan in enumerate(expansion)), reverse=True)
        mx = 0
        i = N - 1
        ans = [None] * N
        for expan, j in sorted_expansion:
            while i > expan:
                ans[i] = mx
                i -= 1
            mx = max(mx, nums[j])
        ans[0] = mx
        return ans

