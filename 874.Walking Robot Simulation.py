class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        res = 0
        obs = set(tuple(ob) for ob in obstacles)
        x = y = face = 0
        direc = (0, 1, 0, -1, 0)
        res = 0
        for cmd in commands:
            if cmd == -1:
                face += 1
                face %= 4
            elif cmd == -2:
                face -= 1
                face %= 4
            else:
                nx, ny = x, y
                for _ in xrange(cmd):
                    nx += direc[face]
                    ny += direc[face + 1]
                    if (nx, ny) in obs:
                        x = nx - direc[face]
                        y = ny - direc[face + 1]
                        break
                else:
                    x, y = nx, ny
                res = max(res, x * x + y * y)
        return res
