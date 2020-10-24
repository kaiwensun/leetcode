class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                if stack[-2] == -stack[-1]:
                    stack.pop()
                    stack.pop()
                elif stack[-2] > -stack[-1]:
                    stack.pop()
                else:
                    stack[-1] = stack.pop()
        return stack

