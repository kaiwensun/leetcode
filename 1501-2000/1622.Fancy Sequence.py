MOD = 10 ** 9 + 7
class Fancy:

    def __init__(self):
        self.val = []  # track base (unit "1")
        self.mul = [1]  # track multiplication
        self.add = [0]  # track (multiplied) additions

    def append(self, val: int) -> None:
        self.val.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc: int) -> None:
        self.add[-1] += inc
        

    def multAll(self, m: int) -> None:
        self.mul[-1] *= m
        self.add[-1] *= m
        

    def getIndex(self, idx: int) -> int:
        if 0 <= idx < len(self.val):
            mul = self.mul[-1] // self.mul[idx]  # calculate multiplication on base
            add = self.add[-1] - self.add[idx] * mul  # subtract the (multiplied) base to get actual (multiplied) addition
            return (self.val[idx] * mul + add) % MOD
        return -1
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

