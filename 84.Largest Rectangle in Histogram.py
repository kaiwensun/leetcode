class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [[0, -1, -1]] # [[height, left_index, right_index], ...]
        res = 0
        for i, height in enumerate(heights + [0]):
            while len(stack) > 1 and stack[-1][0] >= height:
                top = stack.pop()
                res = max(res, top[0] * (top[2] - stack[-1][1]))
                stack[-1][2] = top[2]
            stack.append([height, i, i])
        return res
