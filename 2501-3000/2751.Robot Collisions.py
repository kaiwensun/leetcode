class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted([*info, index] for index, info in enumerate(zip(positions, healths, directions)))
        stack = []
        for robot in robots:
            if robot[2] == "R":
                stack.append(robot)
                continue
            while stack and stack[-1][2] == "R":
                if stack[-1][1] == robot[1]:
                    stack.pop()
                    break
                elif stack[-1][1] > robot[1]:
                    stack[-1][1] -= 1
                    break
                else:
                    stack.pop()
                    robot[1] -= 1
            else:
                stack.append(robot)
        stack.sort(key=lambda robot: robot[3])
        return [robot[1] for robot in stack]

