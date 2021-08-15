class Solution:
    def countArrangement(self, n: int) -> int:
        MAX = n + 1
        multiples = [[] for _ in range(MAX)]
        divisors = [[] for _ in range(MAX)]
        for divisor in range(1, MAX):
            for t in range(1, MAX):
                if divisor * t >= MAX:
                    break
                multiples[divisor].append(divisor * t)
                divisors[divisor * t].append(divisor)
        used = set()
        def dfs(i):
            if i == n + 1:
                return 1
            usables = (set(multiples[i]) | set(divisors[i])) - used
            res = 0
            for usable in usables:
                used.add(usable)
                res += dfs(i + 1)
                used.remove(usable)
            return res

        return dfs(1)

