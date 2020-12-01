class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        stack = []
        for clip in sorted(clips, key=lambda c: (c[0], -c[1])):
            if stack and stack[-1][1] >= clip[1]:
                continue
            if len(stack) >= 2 and stack[-2][1] >= clip[0]:
                stack.pop()
            if stack and (stack[-1][1] < clip[0] or stack[-1][1] >= T):
                break
            stack.append(clip)
        return len(stack) if stack[0][0] == 0 and stack[-1][1] >= T else -1

