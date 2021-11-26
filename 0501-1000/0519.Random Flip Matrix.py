import random

class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.m = m
        self.n = n
        self.inf = (self.m * self.n) ** 1001
        self.rand = random.randint(self.m * self.n, self.inf)
        self.reset()

    def _rand(self):
        if self.rand < self.range:
            raise Error("rand (%d) < range (%d)" % (self.rand, self.range))
        select = self.rand % self.range
        self.rand //= self.range
        self.range -= 1
        return select


    def flip(self):
        """
        :rtype: List[int]
        """
        select = self._rand()
        target = self.range
        while target in self.map:
            if target == self.map[target]:
                raise Error(target)
            target = self.map[target]
        res = select
        while self.map.get(res, res) != res:
            res = self.map[res]
        res = self.map.get(res, res)
        self.map[select] = self.range
        return [res // self.n, res % self.n]


    def reset(self):
        """
        :rtype: None
        """
        self.map = {}
        self.range = self.m * self.n



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
