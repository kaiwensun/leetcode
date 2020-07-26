import functools
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        Aindexes = collections.defaultdict(set)
        for i, a in enumerate(A):
            Aindexes[a].add(i)
        @functools.lru_cache(None)
        def dfs(newA):
            if len(newA) == 0:
                return 0
            i = len(B) - len(newA)
            b = B[i]
            a = newA[0]
            if a == b:
                return dfs(newA[1:])
            mn = float('inf')
            for cand in Aindexes[b]:
                Acand = cand - len(B) + len(newA)
                if Acand <= 0:
                    continue
                if newA[Acand] == B[cand]:
                    continue
                Aindexes[b].remove(cand)
                Aindexes[a].add(cand)
                nextNewA = newA[1:Acand] + a + newA[Acand + 1:]
                mn = min(mn, dfs(nextNewA))
                Aindexes[a].remove(cand)
                Aindexes[b].add(cand)
            return mn + 1
        return dfs(A)
