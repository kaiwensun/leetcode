from collections import Counter, defaultdict

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        cnt = Counter()
        c2vi = defaultdict(lambda: (float('inf'), ""))
        for c, i, v in zip(creators, ids, views):
            cnt[c] += v
            c2vi[c] = min(c2vi[c], (-v, i))
        popularity = max(cnt.values())
        return [[c, c2vi[c][1]] for c in cnt if cnt[c] == popularity]

