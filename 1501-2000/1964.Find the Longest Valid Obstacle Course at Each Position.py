class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = [None] * len(obstacles)
        stack = []
        for i, num in enumerate(obstacles):
            j = bisect.bisect_right(stack, (num, i))
            if j == len(stack):
                stack.append((num, i))
            else:
                stack[j] = (num, i)
            ans[i] = j + 1
        return ans

