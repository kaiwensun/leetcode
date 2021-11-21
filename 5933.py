class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def gen_for_size(size, starter, base):
            if size == 1:
                for i in range(starter, base):
                    yield i
                return
            if size == 2:
                for i in range(starter, base):
                    yield i * base + i
                return
            for new_bit in range(starter, base):
                constant = new_bit * base ** (size - 1) + new_bit
                for inner in gen_for_size(size - 2, 0, base):
                    yield constant + inner * base

        def gen_for_base(base):
            size = 1
            g = gen_for_size(size, 1, base)
            while True:
                num = next(g, None)
                if num is None:
                    size += 1
                    g = gen_for_size(size, 1, base)
                    num = next(g)
                yield num

        gen_k = gen_for_base(k)
        gen_10 = gen_for_base(10)
        res = num_k = num_10 = 0
        n += 1
        while n:
            if num_k == num_10:
                res += num_10
                n -= 1
                num_k = next(gen_k)
                num_10 = next(gen_10)
            elif num_k < num_10:
                num_k = next(gen_k)
            else:
                num_10 = next(gen_10)
        return res

