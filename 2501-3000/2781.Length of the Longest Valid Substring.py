import collections

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        word = "^" + word + "$"
        forbidden.append("$")
        forbidden.append("^")

        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        def put_forbidden(w):
            p = trie
            for c in w:
                p = p[c]
            p["#"] = True

        def get_min_forbidden_size(i):
            p = trie
            size = 0
            while i < len(word):
                c = word[i]
                if c in p:
                    p = p[c]
                    size += 1
                    if p.get("#"):
                        return size
                else:
                    return 0
                i += 1
            return 0

        for forb in forbidden:
            put_forbidden(forb)
        forbidden_intervals = []
        forbidden_intervals_ends = []
        for i in range(len(word)):
            size = get_min_forbidden_size(i)
            if size:
                end = i + size - 1
                forbidden_intervals.append([i, end])
                heapq.heappush(forbidden_intervals_ends, end)
        removed = Counter()
        res = 0
        for interval in forbidden_intervals:
            s, e = interval
            while forbidden_intervals_ends and forbidden_intervals_ends[0] <= s:
                heapq.heappop(forbidden_intervals_ends)
            removed[e] += 1
            while forbidden_intervals_ends and removed[forbidden_intervals_ends[0]]:
                removed[heapq.heappop(forbidden_intervals_ends)] -= 1
            if forbidden_intervals_ends:
                res = max(res, forbidden_intervals_ends[0] - s - 1)
        return res

