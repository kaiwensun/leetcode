import functools, bisect, math

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        robot_data = sorted([[robot, robot - dist, robot + dist] for robot, dist in zip(robots, distance)])
        print(robot_data)
        for i in range(len(robot_data)):
            if i != 0:
                robot_data[i][1] = max(robot_data[i][1], robot_data[i - 1][0] + 1)
            if i != len(robot_data) - 1:
                robot_data[i][2] = min(robot_data[i][2], robot_data[i + 1][0] - 1)
        @functools.cache
        def dp(i: int, right_border: int) -> int:
            if i == -1:
                return 0
            robot, left, right = robot_data[i]
            right = min(right, right_border)
            # shoot to right
            res1 = dp(i - 1, robot - 1) + bisect.bisect_right(walls, right) - bisect.bisect_left(walls, robot)
            # shoot to left
            res2 = dp(i - 1, left - 1) + bisect.bisect_right(walls, robot) - bisect.bisect_left(walls, left)
            return max(res1, res2)
        return dp(len(robot_data) - 1, math.inf)

