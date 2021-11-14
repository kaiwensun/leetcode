class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        self.perimeter = (self.width + self.height) * 2 - 4
        self.posi = 0
        self.dir = 1
        self.moved = False
        self.num = 0


    def move(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.num += num
        self.moved = True

    def _calc(self):
        self.num %= self.perimeter
        if not self.num:
            self.num = self.perimeter
        while self.num:
            nxt = self.posi + self.dir
            if not (0 <= nxt.real < self.width and 0 <= nxt.imag < self.height):
                self.dir *= 1j
                continue
            if self.dir.real:
                step_limit = abs([None, self.width - 1, 0][int(self.dir.real)] - self.posi.real)
            else:
                step_limit = abs([None, self.height - 1, 0][int(self.dir.imag)] - self.posi.imag)
            step = min(step_limit, self.num)
            self.posi += self.dir * step
            self.num -= step
        self.moved = False


    def getPos(self):
        """
        :rtype: List[int]
        """
        if self.moved: self._calc()
        return map(int, [self.posi.real, self.posi.imag])


    def getDir(self):
        """
        :rtype: str
        """
        if self.moved: self._calc()
        return [
            [None, "North", "South"],
            ["East"],
            ["West"],
        ][int(self.dir.real)][int(self.dir.imag)]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

