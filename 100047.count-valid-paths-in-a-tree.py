from functools import cache
from collections import defaultdict

def sieve_of_sundaram(mx):
    if mx < 2:
        return []
    mx_idx = (mx - 1) // 2
    is_prime_idx = [True] * (mx_idx + 1)
    for i in range(1, len(is_prime_idx)):
        if 2 * i * i + i + i > mx_idx:
            break
        for j in range(i, len(is_prime_idx)):
            if 2 * i * j + i + j > mx_idx:
                break
            else:
                is_prime_idx[2 * i * j + i + j] = False
    return [2] + [2 * i + 1 for i, is_prime in enumerate(is_prime_idx) if is_prime and i > 0]

PRIMES = sieve_of_sundaram(10 ** 5)
PRIMES_SET = set(PRIMES)

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        def build_graph(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        @cache
        def dfs(node, parent):
            if node in PRIMES_SET:
                return 0
            res = 1
            for nxt in graph[node]:
                if nxt != parent:
                    res += dfs(nxt, node)
            return res
        graph = build_graph(edges)
        res = 0
        for prime in PRIMES:
            if prime > n:
                break
            cnt_of_a = 1
            cnt_of_path = 0
            for neighbor in graph[prime]:
                branch = dfs(neighbor, prime)
                cnt_of_path += cnt_of_a * branch
                cnt_of_a += branch
            res += cnt_of_path
        return res

