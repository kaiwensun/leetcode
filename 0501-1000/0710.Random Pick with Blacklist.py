class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.map = {}
        self.N = N
        self.total = N - len(blacklist)
        for black in blacklist:
            self.map[black] = -1
        for black in blacklist:
            if black >= self.total:
                continue
            N = N - 1
            while N in self.map:
                N -= 1
            self.map[black] = N
        

    def pick(self):
        """
        :rtype: int
        """
        r = random.randint(0, self.total - 1)
        return self.map.get(r, r)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
