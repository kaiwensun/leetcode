class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        seg_tree = [0] * (n * 2)
        def put(i, value):
            i += n
            while i != 0 and value > seg_tree[i]:
                seg_tree[i] = value
                i //= 2
        def maximum(start, end):
            start += n
            end += n
            mx = 0
            while start < end:
                if start & 1:
                    mx = max(mx, seg_tree[start])
                    start += 1
                if end & 1:
                    end -= 1
                    mx = max(mx, seg_tree[end])
                start //= 2
                end //= 2
            return mx
        left_higher = [None] * n
        nums.append(float("inf"))
        stack = [-1]
        for i in range(n):
            while nums[stack[-1]] <= nums[i]:
                stack.pop()
            left_higher[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(n):
            lh = left_higher[i]
            if lh == -1:
                continue
            my_step = maximum(lh + 1, i) + 1
            put(i, my_step)
            res = max(res, my_step)
        return res

