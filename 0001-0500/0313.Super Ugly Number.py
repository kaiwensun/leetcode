import heapq
class Solution:
    class Line:
        def __init__(self, prime, n, res, seen):
            self.gen = self.generator(prime, n, res, seen)
            
        def generator(self, prime, n, res, seen):
            for i in range(n):
                value = res[i] * prime
                if value not in seen:
                    seen.add(value)
                    while not (yield res[i] * prime):
                        pass
        def get(self):
            return next(self.gen)
        
        def take(self):
            self.gen.send(True)
            return self
        
        def __lt__(self, other):
            return self.get() < other.get()

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglys = [1]
        seen = set(uglys)
        lines = [self.Line(prime, n, uglys, seen) for prime in primes]
        heapq.heapify(lines)
        for i in range(n - 1):
            uglys.append(lines[0].get())
            heapq.heapreplace(lines, lines[0].take())
        return uglys[-1]

# More clever idea by StefanPochmann
# https://leetcode.com/problems/super-ugly-number/discuss/76301/Python-generators-on-a-heap
#
# def nthSuperUglyNumber(self, n, primes):
#     uglies = [1]
#     def gen(prime):
#         for ugly in uglies:
#             yield ugly * prime
#     merged = heapq.merge(*map(gen, primes))
#     while len(uglies) < n:
#         ugly = next(merged)
#         if ugly != uglies[-1]:
#             uglies.append(ugly)
#     return uglies[-1]
