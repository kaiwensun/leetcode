class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        faces = ((0, 1), (-1, 0), (0, -1), (1, 0))
        face_ind = 0
        x, y = 0, 0
        for i in xrange(4):
            for inst in instructions:
                if inst == 'G':
                    face = faces[face_ind]
                    x, y = x + face[0], y + face[1]
                elif inst == 'L':
                    face_ind += 1
                    face_ind %= 4
                elif inst == 'R':
                    face_ind -= 1
                    face_ind %= 4
            if x == y == 0:
                return True
        return False
